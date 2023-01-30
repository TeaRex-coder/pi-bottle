import RPi.GPIO as GPIO
import time

#setup GPIO
sensor = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

def callback_function(sensor):
        if GPIO.input(sensor):
                print ("Alex is out of water :(")
        else:
                print ("Alex has water :)")

GPIO.add_event_detect(sensor, GPIO.BOTH, bouncetime=1000)
GPIO.add_event_callback(sensor, callback_function)

while True:
        time.sleep(0)
