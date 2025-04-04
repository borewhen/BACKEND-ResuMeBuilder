from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required
import numpy as np
import base64
from PIL import Image
from io import BytesIO
from app.service.eye_contact.face_detection import FaceDetector
from app.service.eye_contact.head_pose_estimation import HeadPoseEstimator
from app.service.eye_contact.facial_landmarks_detection import FacialLandmarksDetector
from app.service.eye_contact.gaze_estimation import GazeEstimator
from app.service.eye_contact.main import detect_eye_contact

eye_contact = []
router = APIRouter()
face_detector = FaceDetector("models/face-detection-retail-0004")
facial_landmarks_detector = FacialLandmarksDetector("models/landmarks-regression-retail-0009")
head_pose_estimator = HeadPoseEstimator('models/head-pose-estimation-adas-0001')
gaze_estimator = GazeEstimator('models/gaze-estimation-adas-0002')

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            data = await websocket.receive_text()
            header, encoded = data.split(",", 1)
            decoded = base64.b64decode(encoded)
            
            # Convert image to numpy array
            image = Image.open(BytesIO(decoded)).convert("RGB")
            image = np.array(image)

            # Process frame and count people
            global eye_contact
            eye_contact = detect_eye_contact(face_detector, facial_landmarks_detector, head_pose_estimator, gaze_estimator, image, eye_contact)
            is_making_eye_contact = True if len(eye_contact) < 5 else all(eye_contact)
            # Send back the count
            print("Sending eye contact:", is_making_eye_contact)
            await websocket.send_json({"eye_contact": is_making_eye_contact})

    except Exception as e:
        print("WebSocket Error:", e)
    finally:
        print("Client disconnected")