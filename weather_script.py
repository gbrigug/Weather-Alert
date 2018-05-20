#Powered by Dark Sky
#https:/darksky.net/poweredby/

#Importing libraries
import RPi.GPIO as GPIO
import requests, time

while(1):
    #Notification LED setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)

    #Obtaining weather data
    r = requests.get('https://api.darksky.net/forecast/0157e90ca10eab47efe8f91a3985fb39/39.9524,-75.1636')
    j = r.json() #Decodes JSON object

    for a in range(0,3):
        GPIO.output(17,True)
        time.sleep(.25)
        GPIO.output(17,False)
        time.sleep(.25)

    alert = 0
    for h in range(0,11):
        if j['hourly']['data'][h]['precipProbability'] >= 0.15 and j['hourly']['data'][h]['precipType']== "rain":
            alert = 1

    #Notification LED config
    if alert == 1:
        GPIO.output(17,True)
    else:
        GPIO.output(17,False)
    time.sleep(600)
