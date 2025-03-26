import numpy as np

def detect_eye_contact(face_detector, facial_landmarks_detector, head_pose_estimator, gaze_estimator, frame, eye_contact):
    face_boxes = face_detector.predict(frame)
    face_box = face_boxes[0] if face_boxes else None
    if face_box is None:
        return eye_contact

    face_image = get_crop_image(frame, face_box)
    if face_image.shape[0] == 0 or face_image.shape[1] == 0:
        return eye_contact
    
    eye_boxes, eye_centers = facial_landmarks_detector.predict(face_image)
    if len(eye_boxes) != 2:
        return eye_contact
    
    left_eye_image, right_eye_image = [get_crop_image(face_image, eye_box) for eye_box in eye_boxes]
    if left_eye_image.shape[0] == 0 or left_eye_image.shape[1] == 0 or right_eye_image.shape[0] == 0 or right_eye_image.shape[1] == 0:
        return eye_contact
    
    head_pose_angles = head_pose_estimator.predict(face_image)
    gaze_x, gaze_y = gaze_estimator.predict(right_eye_image, head_pose_angles, left_eye_image)
    gaze_len = np.sqrt(gaze_x**2 + gaze_y**2)
    eye_contact.append(gaze_len < 0.35)
    eye_contact = eye_contact[-5:]
    
    return eye_contact

def get_crop_image(image, box):
    xmin, ymin, xmax, ymax = box
    crop_image = image[ymin:ymax, xmin:xmax]
    return crop_image
