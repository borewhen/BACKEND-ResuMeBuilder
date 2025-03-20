import cv2
import numpy as np
from openvino.runtime import Core

class FacialLandmarksDetector:

    def __init__(self, model_name, device='CPU'):
        self.network = Core().compile_model(model_name+'.xml', device)

    def predict(self, face_image):
        input_image = self._preprocess_input(face_image)
        outputs = self.network(input_image)['95']
        eye_boxes, eye_centers = self._preprocess_output(outputs, face_image)
        return eye_boxes, eye_centers

    def _preprocess_input(self, image):
        n, c, h, w = 1, 3, 48, 48
        input_image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)
        input_image = input_image.transpose((2, 0, 1))
        input_image = input_image.reshape((n, c, h, w))
        return input_image


    def _preprocess_output(self, outputs, image):
        normalized_landmarks = np.squeeze(outputs).reshape((5,2))
        h, w, _ = image.shape
        color = (255,255,255)
        length_offset = int(w * 0.15) 
        eye_boxes, eye_centers = [], []
        for i in range(2):
            normalized_x, normalized_y = normalized_landmarks[i]
            x = int(normalized_x*w)
            y = int(normalized_y*h)
            eye_centers.append([x, y])
            xmin, xmax = max(0, x - length_offset), min(w, x + length_offset)
            ymin, ymax = max(0, y - length_offset), min(h, y + length_offset)
            eye_boxes.append([xmin, ymin, xmax, ymax])
            # cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 1)
        return eye_boxes, eye_centers

        