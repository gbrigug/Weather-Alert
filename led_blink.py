#Importing libraries for Python
import RPi.GPIO as GPIO
import time

#Setting software mode to BCM
GPIO.setmode(GPIO.BCM)
#Setting output pin - based on BCM diagram
GPIO.setup(17, GPIO.OUT)

for i in range(20):
    GPIO.output(17,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)
GPIO.cleanup()
