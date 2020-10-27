#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Class To Manage Well Properties
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class WellTray:
    # Class To Provide Abstract Layer For Accessing Well Rows In 
    # The Well Tray
    # Well Tray Row Numbering Starts From 1
    # Row Towards The Homing Position Is Row 1

    def __init__(self, printer = None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer

    def __get_row_n(self, n = None):
        # Return Y Absolute Position For Nth Row
        if n == None:
            raise TypeError('Required argument missing')
        if(n < 1 or n > MechanicalParameters.well_tray_count_rows):
            return None
        return MechanicalParameters.well_tray_position_origin_mm + \
            MechanicalParameters.well_tray_offset_row1_origin_mm + \
            ((n - 1) * MechanicalParameters.well_tray_offset_inter_row_mm)
    
    def gotoRowN(self, n = None, offset = None):
        # Go To Nth Row
        if n == None:
            raise TypeError('Required argument missing')
        if(n < 1 or n > MechanicalParameters.well_tray_count_rows):
            return None
        self.printer_handle.moveZRelative(MechanicalParameters.well_tray_distance_tip_inserted_mm * -1)
        if offset == None:
            # No Offset Required. Go To Center Of The Well
            self.printer_handle.moveYAbsolute(self.__get_row_n(n))
        elif offset == True:
            # Offset Required
            self.printer_handle.moveYAbsolute(self.__get_row_n(n) + MechanicalParameters.well_tray_offset_from_center_mm)
        self.printer_handle.moveZAbsolute(MechanicalParameters.well_tray_distance_coasting_with_tip_mm + \
            MechanicalParameters.well_tray_distance_tip_inserted_mm)
