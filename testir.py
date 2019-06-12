import RPi.GPIO as GPIO
import time
import os

#to prevent display of warnings
GPIO.setwarnings(False)

#to use configuration on board 
GPIO.setmode(GPIO.BOARD)

"""
GPIO.setmode(GPIO.BCM)
"""

#pin for IR sensor
GPIO.setup(11,GPIO.IN)

#pin for motor
GPIO.setup(13,GPIO.OUT)

#time in which notification can be sent again
time_to_sleep = 7200

while True:

	#reading input from IR sensor
	i = GPIO.input(11)

	#print i
	#NOT logic
	if i == 1:

		#TODO start motor
		os.system('python3 testmotor.py')
		GPIO.output(13,1)
		time.sleep(2)
		GPIO.output(13,0)

		#time.sleep(time_to_sleep)

