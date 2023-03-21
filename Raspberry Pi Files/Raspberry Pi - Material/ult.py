import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
print ("dist measurement in progress")
GPIO.setup(8,GPIO.OUT)
GPIO.setup(5,GPIO.IN)
time.sleep(2)
GPIO.output(8,0)
print  ("waiting for sensor to settle")

while True:
        GPIO.output(8,1)
        time.sleep(0.00001)
        GPIO.output(8,0)

        while GPIO.input(5)==0:
            pulse_start = time.time()

        while GPIO.input(5)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17150
        distance = round(distance,2)
        print ("distance",distance,"cm")
        time.sleep(1)
GPIO.cleanup()
