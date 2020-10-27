#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Class To Manage Magnetic Assembly (Using Servo Motor)
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class Magnet:
    # Class To Provide Abstract Layer For Accessing Magnet Assembly
    # Functionality

    MAGNET_0 = 0
    MAGNET_1 = 1
    
    def __init__(self, printer = None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer
        self.disengageAll()
    
    def engage(self, instance = None):
        # Engage Magnetic Assembly Specific Instance
        if instance == None:
            raise TypeError('Required arguments missing')
        if instance not in MechanicalParameters.servo_ports:
            BaseLogger.error('invalid servo port')
            return
        self.printer_handle.moveServo(instance, \
            MechanicalParameters.servo_position_degree_engaged[instance])

    def engageAll(self):
        # Engage Magnetic Assembly All Instance
        for instance in MechanicalParameters.servo_ports:
            self.printer_handle.moveServo(instance, \
                MechanicalParameters.servo_position_degree_engaged[instance])
    
    def disengage(self, instance = None):
        # Disengage Magnetic Assembly Specific Instance
        if instance == None:
            raise TypeError('Required arguments missing')
        if instance not in MechanicalParameters.servo_ports:
            BaseLogger.error('invalid servo port')
            return
        self.printer_handle.moveServo(instance, \
            MechanicalParameters.servo_position_degree_disengaged[instance])

    def disengageAll(self):
        # Disengage Magnetic Assembly All Instance
        for instance in MechanicalParameters.servo_ports:
            self.printer_handle.moveServo(instance, \
                MechanicalParameters.servo_position_degree_disengaged[instance])
    
