import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD) 

GPIO.setwarnings(False) 

GPIO.setup(3,GPIO.IN) 

GPIO.setup(5,GPIO.IN) 

GPIO.setup(7,GPIO.OUT) 

GPIO.setup(11,GPIO.OUT) 

while True: 

    if GPIO.input(3)==1: 

        GPIO.output(7,1)  

        GPIO.output(11,0) 

        '''print ("RED")'''

        time.sleep(0.1)

    elif GPIO.input(5)==1: 

        GPIO.output(7,0)  

        GPIO.output(11,1) 

        '''print ("GREEN")'''

        time.sleep(0.1)

GPIO.cleanup()
 