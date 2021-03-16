from gpiozero import MotionSensor

class MotionDetector:

    def __init__(self):
        self.pir = MotionSensor(4)

    def movement_detected(self):
        return bool(self.pir.motion_detected)
