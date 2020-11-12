#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Printer Thread
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import time
import subprocess
from parse import parse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from threads.MKSCheck import MKSCheck
from classes.MKSSerialCommunication import MKSSerialCommunication
from helpers.BaseLogger import BaseLogger
from helpers.USB import *

class Printer(QtCore.QThread):
    # Printer Communication Thread

    # G-Codes
    gcode_move = 'G1 X{0} Y{1} Z{2} F6000'
    gcode_move_x = 'G1 X{0} F2000'
    gcode_move_y = 'G1 Y{0} F6000'
    gcode_move_z = 'G1 Z{0} F2000'
    gcode_move_e = 'G1 E{0} F2000'
    gcode_home = 'G28 X Y Z'
    gcode_home_x = 'G28 X'
    gcode_home_y = 'G28 Y'
    gcode_home_z = 'G28 Z'
    gcode_postion_absolute = 'G90'
    gcode_postion_relative = 'G91'
    gcode_serial_print = 'M118 {0}'
    gcode_finish_moves = 'M400'
    gcode_get_current_position = 'M114'
    gcode_move_servo = 'M280 P{0} S{1}'
    gcode_get_pos_servo = 'M280 P{0}'
    gcode_set_temp_unit_c = 'M149 C'
    gcode_set_bed_temp = 'M190 R{0}'
    gcode_set_extruder_pos = 'G92 E0'

    mks_serial_comm = None
    ui_reference = None
    connected = False
    homed = False
    current_position = [0, 0]

    def __init__(self, ui_reference):
        super(Printer, self).__init__()
        self.connected = False
        self.mks_port = None     
        self.ui_reference = ui_reference

    def getConnectedStatus(self):
        # Return MKS Connection Status
        return self.connected

    def getHomingStatus(self):
        # Return Homing Status
        return self.homed

    def getPort(self):
        # Return MKS Serial Port Identifier
        return self.mks_port
    
    def getCurrentPosition(self):
        # Return Current Position
        return self.current_position

    def waitTillResponseOK(self):
        # Blocking Wait Till 'ok' Response Received
        self.response_type = 'RESPONSE_TYPE_BUSY'
        while self.response_type != 'RESPONSE_TYPE_OK':
            self.response = self.mks_serial_comm.getResponse()
            self.response_type = self.parseResponseType(self.response)
    
    def waitTillResponsePosition(self):
        # Blocking Wait Till Position Response Received
        self.response_type = 'RESPONSE_TYPE_BUSY'
        while self.response_type != 'RESPONSE_TYPE_POSITION':
            self.response = self.mks_serial_comm.getResponse()
            self.response_type = self.parseResponseType(self.response)
    
    def parseResponseType(self, response):
        # Check The Response Type Received From MKS
        if 'echo:busy: processing' in response:
            return 'RESPONSE_TYPE_BUSY'
        if 'ok' in response:
            return 'RESPONSE_TYPE_OK'
        if 'X:' in response:
            # Parse Position Response To Save Print Head Position
            parse_result = parse('X:{} Y:{} Z:{} E:{}', response)
            self.current_position = [parse_result[1], parse_result[2]]
            return 'RESPONSE_TYPE_POSITION'
        return 'RESPONSE_TYPE_OTHER'

    def run(self):
        BaseLogger.info('Initializing Printer ...')

        self._thread_mks_check = MKSCheck()
        self._thread_mks_check.start()

        # Wait For MKS Checking To Finish
        # Check If Initialized Properly
        self._thread_mks_check.wait()
        if(not bool(self._thread_mks_check.getStatus())):
            BaseLogger.info('Hardware Error ... HALTING')
            while(True):
                pass

        # Create MKS Serial Connection
        self.mks_serial_comm = MKSSerialCommunication(self._thread_mks_check.getPort(), 115200)
        self.connected = True

        # Set Printer Parameters
        BaseLogger.info('Setting Printer Parameters ...')
        self.positionAbsolute()
        self.temperatureCelcius()

        # Printer Home
        BaseLogger.info('Homing Printer ...')
        self.moveServo(0, 0)
        self.home()

        
        self.homed = True
        
        # Run Thread Indefinitly
        while True:
            pass
    '''
    **********************************
    * Printer GCode Routines
    **********************************
    * Homing
    **********************************
    '''
    def home(self):
        self.homeX()
        self.homeZ()
        self.homeY()
    
    def homeX(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_home_x)
            self.waitTillResponseOK()
    
    def homeY(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_home_y)
            self.waitTillResponseOK()
    
    def homeZ(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_home_z)
            self.waitTillResponseOK()
    
    '''
    **********************************
    * Movement
    **********************************
    '''
    def positionRelative(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_postion_relative)
            self.waitTillResponseOK()
    
    def positionAbsolute(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_postion_absolute)
            self.waitTillResponseOK()
    
    def moveXAbsolute(self, x):
        # Move X Axis Absolute mm
        if(bool(self.connected)):
            self.positionAbsolute()
            self.mks_serial_comm.sendCommand(self.gcode_move_x.format(x))
            self.waitTillResponseOK()
            self.finishMoves()
            self.serialPrint('ok done')
            self.getPosition()

    def moveXRelative(self, x):
        # Move X Axis Relative Distance mm
        if(bool(self.connected)):
            self.positionRelative()
            self.mks_serial_comm.sendCommand(self.gcode_move_x.format(x))
            self.waitTillResponseOK()
            self.finishMoves()
            self.positionAbsolute()
            self.serialPrint('ok done')
            self.getPosition()
    
    def moveYAbsolute(self, y):
        # Move Y Axis Absolute mm
        if(bool(self.connected)):
            self.positionAbsolute()
            self.mks_serial_comm.sendCommand(self.gcode_move_y.format(y))
            self.waitTillResponseOK()
            self.finishMoves()
            self.serialPrint('ok done')
            self.getPosition()

    def moveYRelative(self, y):
        # Move Y Axis Relative Distance mm
        if(bool(self.connected)):
            self.positionRelative()
            self.mks_serial_comm.sendCommand(self.gcode_move_y.format(y))
            self.waitTillResponseOK()
            self.finishMoves()
            self.positionAbsolute()
            self.serialPrint('ok done')
            self.getPosition()

    def moveZAbsolute(self, z):
        # Move Z Axis Absolute mm
        if(bool(self.connected)):
            self.positionAbsolute()
            self.mks_serial_comm.sendCommand(self.gcode_move_z.format(z))
            self.waitTillResponseOK()
            self.finishMoves()
            self.serialPrint('ok done')
            self.getPosition()

    def moveZRelative(self, z):
        # Move Z Axis Relative Distance mm
        if(bool(self.connected)):
            self.positionRelative()
            self.mks_serial_comm.sendCommand(self.gcode_move_z.format(z))
            self.waitTillResponseOK()
            self.finishMoves()
            self.positionAbsolute()
            self.serialPrint('ok done')
            self.getPosition()
    
    def moveEAbsolute(self, e):
        # Move E Axis Absolute mm
        if(bool(self.connected)):
            self.positionAbsolute()
            self.mks_serial_comm.sendCommand(self.gcode_move_e.format(e))
            self.waitTillResponseOK()
            self.finishMoves()
            self.serialPrint('ok done')
            self.getPosition()
    
    def moveERelative(self, e):
        # Move E Axis Relative Distance mm
        if(bool(self.connected)):
            self.positionRelative()
            self.mks_serial_comm.sendCommand(self.gcode_move_e.format(e))
            self.waitTillResponseOK()
            self.finishMoves()
            self.positionAbsolute()
            self.serialPrint('ok done')
            self.getPosition()

    def move(self, x, y, z):
        if(bool(self.connected)):
            self.positionRelative()
            self.mks_serial_comm.sendCommand(self.gcode_move.format(x, y, z))
            self.waitTillResponseOK()
            self.finishMoves()
            self.positionAbsolute()
            self.serialPrint('ok done')
            self.getPosition()
    
    '''
    **********************************
    * Servo
    **********************************
    '''
    def moveServo(self, port, angle_pos):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_move_servo.format(port, angle_pos))
            self.waitTillResponseOK()
    
    '''
    **********************************
    * Temperature
    **********************************
    '''
    def temperatureCelcius(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_set_temp_unit_c)
            self.waitTillResponseOK()
    
    def setBedTemperature(self, temp):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_set_bed_temp.format(temp))
            self.waitTillResponseOK()

    '''
    **********************************
    * Misc
    **********************************
    '''
    def serialPrint(self, string):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_serial_print.format(string))
            self.waitTillResponseOK()
        
    def finishMoves(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_finish_moves)
            self.waitTillResponseOK()

    def getPosition(self):
        if(bool(self.connected)):
            self.mks_serial_comm.sendCommand(self.gcode_get_current_position)
            self.waitTillResponsePosition()