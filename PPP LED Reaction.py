import RPi.GPIO as GPIO
import time
import random
from datetime import datetime

GPIO.setmode(GPIO.BOARD)    #use GPIO board numbers

GPIO.setup(16, GPIO.OUT)    #set pin 16 as output (LED)
GPIO.setup(22, GPIO.IN)     #set pin 22 as input (button)

GPIO.output(16, False)      #switch off LED
random.seed()               #seed random

while True:
    time.sleep(random.random()*10)  #sleep forrandom secs
    start = datetime.now()          #record start time
    GPIO.output(16, True)           #switch on LED
    while not GPIO.input(22):       #while button NOT pressed
        pass
    print("Reaction Time :",        #here if IS button pressed
          (datetime.now() - start).total_seconds()) #rection time
    GPIO.output(16, False)      #switch off LED
    print("Try again ...")
