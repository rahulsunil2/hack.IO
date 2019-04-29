import os
import time
from picamera import PiCamera
from signal import pause


destination = '/home/pi/train'
camera = PiCamera()

filename = os.path.join(destination, dt.datetime.now().strftime('%Y-%m-%d_%H%M.h264'))
camera.start_recording(filename)
camera.wait_recording(3600)
camera.stop_recording()
time.sleep(1)