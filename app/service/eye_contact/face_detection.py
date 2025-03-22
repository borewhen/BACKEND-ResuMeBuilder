import cv2
from openvino.runtime import Core

class FaceDetector:
    '''
    Class for the Face Detection Model.
    '''
    def __init__(self, model_name, device='CPU', threshold=0.60):
        self.threshold = threshold
        self.network = Core().compile_model(model_name+'.xml', device)

    def predict(self, image):
        input_image = self._preprocess_input(image)
        outputs = self.network(input_image)['detection_out']
        face_boxes = self._preprocess_output(outputs, image)
        return face_boxes

    def _preprocess_input(self, image):
        n, c, h, w = 1, 3, 300, 300
        input_image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)
        input_image = input_image.transpose((2, 0, 1))
        input_image = input_image.reshape((n, c, h, w))
        return input_image

    def _preprocess_output(self, outputs, image):
        face_boxes = []
        h, w, _ = image.shape
        color = (255,0,0)
        for obj in outputs[0][0]:
            if obj[2] > self.threshold:
                xmin = int(obj[3] * w)
                ymin = int(obj[4] * h)
                xmax = int(obj[5] * w)
                ymax = int(obj[6] * h)
                face_boxes.append([xmin, ymin, xmax, ymax])
                # cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 1)
        return face_boxes