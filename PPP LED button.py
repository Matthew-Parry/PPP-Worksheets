import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    #use GPIO board numbers

GPIO.setup(16, GPIO.OUT)    #set pin 11 as output (LED)
GPIO.setup(22, GPIO.IN)     #set pin 22 as input (button)

while True:
    if GPIO.input(22):          #if button is pressed
        GPIO.output(16, True)   #switch on LED
    else:
        GPIO.output(16, False)  #switch off LED
    time.sleep(0.1)
