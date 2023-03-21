import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
while True:
        
        print("ON")
        GPIO.output(3,1)
        time.sleep(1)

        print("OFF")
        GPIO.output(3,0)
        time.sleep(1)

GPIO.cleanup()         
