import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(3,GPIO.OUT)

GPIO.setup(5,GPIO.OUT)

GPIO.setup(7,GPIO.OUT)

while True:

    GPIO.output(3,1) 

    GPIO.output(5,0)

    GPIO.output(7,0)

    print("RED")

    time.sleep(10)


    GPIO.output(3,0) 

    GPIO.output(5,1)

    GPIO.output(7,0)
 
    print("GREEN")

    time.sleep(5)


    GPIO.output(3,0) 

    GPIO.output(5,0)

    GPIO.output(7,1)
   
    print("YELLOW")

    time.sleep(2)

GPIO.cleanup()



