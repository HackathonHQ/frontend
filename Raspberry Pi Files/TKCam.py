import tkinter as tk
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
camera = PiCamera()
timestamp = datetime.now().isoformat()
camera.capture('/home/pi/%s.jpg' % timestamp)
pause()
 
