import cv2
import numpy as np
import math
from openvino.runtime import Core

class GazeEstimator:

    def __init__(self, model_name, device='CPU', extensions=None):
        self.network = Core().compile_model(model_name+'.xml', device)

    def predict(self, right_eye_image, head_pose_angles, left_eye_image):
        _, _, roll = head_pose_angles
        right_eye_image, head_pose_angles, left_eye_image = self._preprocess_input(right_eye_image, head_pose_angles, left_eye_image)
        input_dict = {"left_eye_image": left_eye_image, "right_eye_image": right_eye_image, "head_pose_angles": head_pose_angles}
        outputs = self.network(input_dict)['gaze_vector']
        gaze_vector = self._preprocess_output(outputs, roll)
        return gaze_vector

    def _preprocess_input(self, right_eye_image, head_pose_angles, left_eye_image):
        left_eye_image = self._preprocess_eye_image(left_eye_image)
        right_eye_image = self._preprocess_eye_image(right_eye_image)
        head_pose_angles = self._preprocess_angels(head_pose_angles)
        return right_eye_image, head_pose_angles, left_eye_image

    def _preprocess_angels(self, head_pose_angles):
        input_shape = (1, 3)
        head_pose_angles = np.reshape(head_pose_angles, input_shape)
        return head_pose_angles

    def _preprocess_eye_image(self, image):
        n, c, h, w = 1, 3, 60, 60
        input_image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)
        input_image = input_image.transpose((2, 0, 1))
        input_image = input_image.reshape((n, c, h, w))
        return input_image

    def _preprocess_output(self, outputs, roll):

        gaze_vector = outputs[0]
        gaze_vector_n = gaze_vector / np.linalg.norm(gaze_vector)
        vcos = math.cos(math.radians(roll))
        vsin = math.sin(math.radians(roll))
        x =  gaze_vector_n[0]*vcos + gaze_vector_n[1]*vsin
        y = -gaze_vector_n[0]*vsin + gaze_vector_n[1]*vcos
        return [x, y]