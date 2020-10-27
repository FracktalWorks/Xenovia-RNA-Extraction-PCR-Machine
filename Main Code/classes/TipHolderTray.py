#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Class To Manage Tip Holder Properties
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class TipHolderTray:
    # Class To Provide Abstract Layer For Accessing Tips
    # In The Tip Holder Tray
    # Tip Holder Tray Row Numbering Starts From 1
    # Row Towards The Homing Position Is Row 1
    
    count_current_row = 1

    def __init__(self, printer=None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer

    def reset(self):
        # Reset Current Row Count
        self.count_current_row = 1;

    def getRowN(self, n):
        # Return Y Absolute Position For Nth Row
        if(n < 1 or n > MechanicalParameters.well_tray_count_rows):
            return
        return MechanicalParameters.tip_tray_position_origin_mm + MechanicalParameters.tip_tray_offset_row1_origin_mm + ((n - 1) * MechanicalParameters.tip_tray_offset_inter_row_mm)

    def getTipsRowN(self, n):
        # Pick Up Tips From Nth Row
        if(n < 1 or n > MechanicalParameters.well_tray_count_rows):
            return
        self.printer_handle.homeZ()
        self.printer_handle.moveYAbsolute(self.getRowN(n))
        self.printer_handle.moveZAbsolute(MechanicalParameters.tip_tray_distance_pipette_tip_lock_mm)
        self.printer_handle.moveZAbsolute(MechanicalParameters.tip_tray_distance_coasting_with_tip_mm)
    
    def getTips(self):
        # Pick Up Tips From The Next Available Row
        if(self.count_current_row > MechanicalParameters.well_tray_count_rows):
            return
        self.getTipsRowN(self.count_current_row)
        self.count_current_row += 1