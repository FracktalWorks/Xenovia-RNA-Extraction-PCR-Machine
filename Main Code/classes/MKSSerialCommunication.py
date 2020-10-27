#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * MKS Gen 1.4 Serial Communication
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
import time
import serial

from helpers.BaseLogger import BaseLogger

class MKSSerialCommunication():

    serial_opening_wait = 2
    serial_response_wait = 0.1

    def __init__(self, serialport=None, serialspeed=None):
        if not serialport or not serialspeed:
            raise TypeError('Required arguments missing')
        self.serial_port = serialport
        self.serial_speed = serialspeed
        # Open Serial Port
        # Give 5 Second Delay For Port To Finish Opening
        # Flash Any Garbage That Comes In Between
        BaseLogger.info('Opening Serial Port ' + self.serial_port + ' @ ' + str(self.serial_speed))
        self.serial_handle = serial.Serial(self.serial_port, self.serial_speed)
        time.sleep(self.serial_opening_wait)
        self.serial_handle.flushInput()
        if(self.serial_handle):
            BaseLogger.info('Serial Port Opened ...')
        else:
            BaseLogger.info('Serial Port Error ...')

    def sendCommand(self, command=None):
        # Send Serial Command To MKS
        if not command:
            raise TypeError('Required arguments missing')
        self.serial_command = '%s\r\n' % command
        self.serial_handle.write(self.serial_command.encode())
        BaseLogger.debug('<<< ' + self.serial_command.rstrip())
    
    def getResponse(self):
        # Get Incoming Response Data From MKS If Any
        time.sleep(self.serial_response_wait)
        self.serial_response = self.serial_handle.readline()
        if self.serial_response:
            BaseLogger.debug('>>> ' + self.serial_response.decode().rstrip())
            return self.serial_response.decode()
        return None