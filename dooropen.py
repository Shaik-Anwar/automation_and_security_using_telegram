import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep      # Importing sleep from time library to add delay in code

servo_pin = 18      # Initializing the GPIO 21 for servo motor

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin

p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
p.start(2.5)
p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
sleep(1)                # Delay of 1 sec
GPIO.cleanup()              # Make all GPIO pins LOW
