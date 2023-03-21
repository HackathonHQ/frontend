import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
pwm=GPIO.PWM(3,50)
pwm.start(0)
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)
SetAngle(90)
pwm.stop()
GPIO.cleanup()
