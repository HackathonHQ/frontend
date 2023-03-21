import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN) 
GPIO.setup(5,GPIO.IN) 
GPIO.setup(7,GPIO.OUT) #GPIO 7 -> Motor 1 terminal A
GPIO.setup(8,GPIO.OUT) #GPIO 8 -> Motor 1 terminal B

GPIO.setup(11,GPIO.OUT) #GPIO 11 -> Motor Left terminal A
GPIO.setup(12,GPIO.OUT) #GPIO 12 -> Motor Left terminal B

while 1:

 

    if(GPIO.input(3)==True and GPIO.input(5)==True): #both while move forward     
        GPIO.output(7,True) #1A+
        GPIO.output(8,False) #1B-

        GPIO.output(11,True) #3A+
        GPIO.output(12,False) #3B-

    elif(GPIO.input(3)==False and GPIO.input(5)==True): #turn right  
        GPIO.output(7,True) #1A+
        GPIO.output(8,True) #1B-

        GPIO.output(11,True) #3A+
        GPIO.output(12,False) #3B-

    elif(GPIO.input(3)==True and GPIO.input(5)==False): #turn left
        GPIO.output(7,True) #1A+
        GPIO.output(8,False) #1B-

        GPIO.output(11,True) #3A+
        GPIO.output(12,True) #3B-

    else:  #stay still
        GPIO.output(7,True) #1A+
        GPIO.output(8,True) #1B-

        GPIO.output(11,True) #3A+
        GPIO.output(12,True) #3B-




