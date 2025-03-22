import cv2
from openvino.runtime import Core

class HeadPoseEstimator:
    '''
    Class for the Head Pose Estimation Model.
    '''
    def __init__(self, model_name, device='CPU', extensions=None):
        self.network = Core().compile_model(model_name+'.xml', device)

    def predict(self, image):
        input_image = self._preprocess_input(image)
        outputs = self.network(input_image)
        head_pose_angles = self._preprocess_output(outputs, image)
        return head_pose_angles

    def _preprocess_input(self, image):
        n, c, h, w = 1, 3, 60, 60
        input_image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)
        input_image = input_image.transpose((2, 0, 1))
        input_image = input_image.reshape((n, c, h, w))
        return input_image


    def _preprocess_output(self, outputs, image):
        yaw = outputs['angle_y_fc'][0][0]
        pitch = outputs['angle_p_fc'][0][0]
        roll = outputs['angle_r_fc'][0][0]
        return [yaw, pitch, roll]