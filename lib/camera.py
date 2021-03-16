import subprocess
import time
import os

from picamera import PiCamera

class Camera:

    def __init__(self, folder):
        self.camera = PiCamera()
        self.registration_folder = os.path.abspath(folder)
        self.record = {}

    def start_recording(self, delay=60):
        video_h264 = os.path.join(self.registration_folder, 'vid-' + time.strftime("%H%M%S-%Y%m%d") + '.h264')
        video_mp4 = os.path.join(self.registration_folder, 'vid-' + time.strftime("%H%M%S-%Y%m%d") + '.mp4')
        self.camera.start_recording(video_h264)
        time.sleep(int(delay))
        self.camera.stop_recording()

        error = self.__convert_h264_to_mp4(video_h264, video_mp4)
        self.record = {
            "name": video_mp4,
            "return_code": error,
        }
        return self.record

    @staticmethod
    def __convert_h264_to_mp4(h264, mp4):
        command = "MP4Box -add {} {}".format(h264, mp4)
        try:
            subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as err:
            error = 'FAIL:\ncmd:{}\noutput:{}'.format(err.cmd, err.output)
            return error
        else:
            return None

    def take_photo(self):
        photo = os.path.join(self.registration_folder, 'photo-' + time.strftime("%H%M%S-%Y%m%d") + '.jpeg')
        self.camera.capture(photo)
        return photo

    def __del__(self):
        self.camera.close()

    def purge_records(self):
        command = "cd " + self.registration_folder + " && rm -rf *.h264 *.mp4 .jpeg"
        try:
            subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as err:
            result = 'FAIL:\ncmd:{}\noutput:{}'.format(err.cmd, err.output)
            return result
        else:
            result = 'The records have been deleted'
            return result