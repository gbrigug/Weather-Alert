#Importing libraries
import RPi.GPIO as GPIO
import requests

#Obtaining weather data
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4560349&units=imperial&APPID=03967c261c3e2f58cf796b6b000e855b')
j = r.json() #Decodes JSON object

key = 'rain'
if key not in j:
    alert = 0
    print "No rain data is available."
else:
    alert = 1

#Notification LED config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

if alert == 1:
    GPIO.output(17,True)
else:
    GPIO.output(17,False)
