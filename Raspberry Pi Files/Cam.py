from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.capture('/home/pi/Desktop/Pycam2.jpg')
