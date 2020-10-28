#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Class To Manage Pipette
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import time

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class Pipette:
    # Class To Provide Abstract Layer For Accessing Pipette
    # Functionality

    PIPETTE_LEVEL_UL_50 = 0
    PIPETTE_LEVEL_UL_100 = 1
    PIPETTE_LEVEL_UL_150 = 2
    PIPETTE_LEVEL_UL_200 = 3
    
    def __init__(self, printer=None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer

    def __isValidLevel(self, level = None):
        # Check If Pipette Liquid Level Is Valid
        if level == None:
            raise TypeError('Required argument missing')
        return level in range(MechanicalParameters.pipette_level_count)
    
    def aspirate(self, level = None):
        # Pipette Aspirate Action
        if level == None:
            raise TypeError('Pipette level missing')
        if not bool(self.__isValidLevel(level)):
            BaseLogger.error('invalid pipette level')
        self.printer_handle.moveXAbsolute( \
            MechanicalParameters.pipette_distance_aspirate_min_mm[level])

    def dispense(self):
        # Pipette Dispense Action
        self.printer_handle.moveXAbsolute(MechanicalParameters.pipette_distance_aspirate_max_mm)
    
    def pump(self, level = None, cycle_count = None, delay_sec_1 = None, delay_sec_2 = None):
        # Run Pipette Aspire - Dispense Cycle (Pump Cyle) cycle_count Times
        # delay_sec_1 Delay Between Aspirating and Dispensing
        # delay_sec_2 Delay Between Pump Cycles 
        if level == None or cycle_count == None or delay_sec_1 == None or delay_sec_2 == None:
            raise typeError('Required argument missing')
        if not bool(self.__isValidLevel(level)):
            BaseLogger.error('invalid pipette level')
        for i in range(cycle_count):
            self.aspirate(level)
            time.sleep(delay_sec_1)
            self.dispense()
            time.sleep(delay_sec_2)
