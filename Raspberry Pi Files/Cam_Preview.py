from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.start_preview()
#sleep(50)
#camera.stop_preview()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/Grandpa.jpg')
camera.stop_preview()
