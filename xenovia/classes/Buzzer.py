#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Buzzer Helper Routines
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import time
import RPi.GPIO as GPIO

from helpers.Run_Async import Run_Async

# Use the board numbering scheme
GPIO.setmode(GPIO.BCM)

# Disable GPIO warnings
GPIO.setwarnings(False)

class Buzzer(object):
    def __init__(self, buzzerPin):
        GPIO.cleanup()
        self.buzzerPin = buzzerPin
        GPIO.setup(self.buzzerPin, GPIO.OUT)
        GPIO.output(self.buzzerPin, GPIO.LOW)

    @Run_Async
    def On(self):
        GPIO.output(self.buzzerPin, (GPIO.HIGH))

    @Run_Async
    def Off(self):
        GPIO.output(self.buzzerPin, (GPIO.LOW))
        
    @Run_Async
    def Beep(self, time_sec):
        GPIO.output(self.buzzerPin, (GPIO.HIGH))
        time.sleep(time_sec)
        GPIO.output(self.buzzerPin, GPIO.LOW)