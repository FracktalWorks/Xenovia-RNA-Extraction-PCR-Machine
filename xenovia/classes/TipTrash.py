#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: June 2020
 *
 * Class To Manage Well Properties
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

from classes.Tip import Tip
from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class TipTrash:
    # Class To Provide Abstract Layer For Accessing Tip Trashing
    # Functionality

    def __init__(self, printer=None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer

    def trashTips(self):
        # Trash Tips
        self.printer_handle.moveZAbsolute(MechanicalParameters.tip_trash_distance_coasting_with_tip_mm)
        self.printer_handle.moveYAbsolute(MechanicalParameters.tip_trash_position_groove_mm)
        self.printer_handle.moveZRelative(MechanicalParameters.tip_trash_distance_tip_groove_unlocking_mm)
        self.printer_handle.moveYRelative(MechanicalParameters.tip_trash_offset_tip_groove_size_mm)
        self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_distance_tip_groove_locking_mm)
        self.printer_handle.moveZRelative(MechanicalParameters.tip_trash_distance_tip_groove_locking_mm)
        self.printer_handle.moveYAbsolute(MechanicalParameters.tip_trash_position_origin_mm)
        
        #self.printer_handle.moveZAbsolute(MechanicalParameters.tip_trash_distance_tip_groove_locking_mm)
        #
        #self.printer_handle.moveZAbsolute(MechanicalParameters.tip_trash_distance_tip_groove_locking_mm)
        #self.printer_handle.moveYRelative(-1 * MechanicalParameters.tip_trash_position_groove_mm)
        #self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_position_groove_mm)
        #self.printer_handle.moveZAbsolute(MechanicalParameters.tip_trash_distance_coasting_with_tip_mm)
        #self.printer_handle.moveYRelative(MechanicalParameters.tip_trash_offset_tip_groove_size_mm)
        #self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_position_origin_mm )
        #self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_distance_tip_groove_unlocking_mm)
        #self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_position_groove_mm)
        #self.printer_handle.moveZRelative(-1 * MechanicalParameters.tip_trash_position_origin_mm )
        

    def moveToTrash(self):
        # Trash Tips
        self.printer_handle.moveZAbsolute(MechanicalParameters.tip_trash_distance_coasting_with_tip_mm)
        self.printer_handle.moveYAbsolute(MechanicalParameters.tip_trash_position_groove_mm)
    