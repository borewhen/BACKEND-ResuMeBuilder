import cv2
import logging as log
import numpy as np

from face_detection import FaceDetector
from head_pose_estimation import HeadPoseEstimator
from facial_landmarks_detection import FacialLandmarksDetector
from gaze_estimation import GazeEstimator

def main():
    face_detector = FaceDetector("models/face-detection-retail-0004")
    facial_landmarks_detector = FacialLandmarksDetector("models/landmarks-regression-retail-0009")
    head_pose_estimator = HeadPoseEstimator('models/head-pose-estimation-adas-0001')
    gaze_estimator = GazeEstimator('models/gaze-estimation-adas-0002')
    
    cap = cv2.VideoCapture(0)
    eye_contact = []
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        face_boxes = face_detector.predict(frame)
        for face_box in face_boxes:
            face_image = get_crop_image(frame, face_box)
            eye_boxes, eye_centers = facial_landmarks_detector.predict(face_image)
            left_eye_image, right_eye_image = [get_crop_image(face_image, eye_box) for eye_box in eye_boxes]
            head_pose_angles = head_pose_estimator.predict(face_image)
            gaze_x, gaze_y = gaze_estimator.predict(right_eye_image, head_pose_angles, left_eye_image)
            # draw_gaze_line(frame, face_box, eye_centers, gaze_x, gaze_y)
            gaze_len = np.sqrt(gaze_x**2 + gaze_y**2)
            eye_contact.append(gaze_len < 0.35)
            eye_contact = eye_contact[-5:]
            if sum(eye_contact) == 0:
                cv2.putText(frame, f'Please Maintain Eye Contact With the Interviewer!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('im', frame)

        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord('q'):
            break
        elif key_pressed == ord(' '):
            cv2.waitKey(0)
            
    cap.release()
    cv2.destroyAllWindows()

def get_crop_image(image, box):
    xmin, ymin, xmax, ymax = box
    crop_image = image[ymin:ymax, xmin:xmax]
    return crop_image


def draw_gaze_line(image, face_box, eye_centers, gaze_x, gaze_y):
    xmin, ymin, xmax, ymax = face_box
    for x, y in eye_centers:
        start = (x+xmin, y+ymin)
        end = (x+xmin+int(gaze_x*3000), y+ymin-int(gaze_y*3000))
        beam_image = np.zeros(image.shape, np.uint8)
        for t in range(20)[::-2]:
            cv2.line(beam_image, start, end, (0, 0, 255-t*10), t*2)
        image |= beam_image
        
def detect_eye_contact(image, gaze_x, gaze_y, threshold=0.3):
    gaze_len = np.sqrt(gaze_x**2 + gaze_y**2)
    cv2.putText(image, f'Eye Contact: {gaze_len < 0.35}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
if __name__ == '__main__':
    main()