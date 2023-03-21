import tkinter as tk
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep
from signal import pause
camera = PiCamera()
timestamp = datetime.now().isoformat()
camera.start_recording('/home/pi/ThePeriodicTable.h264')
sleep(30)
camera.stop_recording()
pause()
 
