import RPi.GPIO as GPIO
import time

#GPIO Basic initialization 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

#LED configuration
led = 17
GPIO.setup(led, GPIO.OUT)

#Turn on the LED 
print("LED on") 
GPIO.output(led, GPIO.HIGH)

#Wait 5s
time.sleep(5) 

#Turn off the LED 
print("LED off") 
GPIO.output(led, GPIO.LOW) 