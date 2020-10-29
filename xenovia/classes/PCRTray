#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar, Vijay Raghav Varada
 * Created: May 2020
 *
 * Class To Manage PCR Tray Properties
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger


class PCRTray:
    """
    Class To Provide Abstract Layer For Accessing PCR Rows In The PCR Tray.
    PCR Tray Row Numbering Starts From 1
    Row Towards The Homing Position is Row 1
    """

    def __init__(self, printer=None):
        if not printer:
            raise TypeError('Required argument missing')
        self.printer_handle = printer

    def __get_row_n(self, n=None):
        """
        Method that returns absolute position of Nth row of PCR tray wrt printer home.
        Args:
            n (int):            row to get position of
        Raises:
            TypeError:          If required row is'nt passed
        Returns:
            (float):            Absolute position of PCR row
        """
        # Return Y Absolute Position For Nth Row
        if n == None:
            raise TypeError('Required argument missing')
        if (n < 1 or n > MechanicalParameters.PCR_tray_count_rows):
            return None
        return MechanicalParameters.PCR_tray_position_origin_mm + \
               MechanicalParameters.PCR_tray_offset_row1_origin_mm + \
               ((n - 1) * MechanicalParameters.PCR_tray_offset_inter_row_mm)

    def gotoRowN(self, n=None, offset=None):
        """
        Method that tells the printer to move Pipette head to move to Nth row of PCR tray
        Args:
            n (int):              The row to move to, index starts from 1
            offset (float):       offset added to the position if needed
        Raises:
            TypeError:            If required row isn't parsed
        Returns:
            None
        """
        if n == None:
            raise TypeError('Required argument missing')
        if (n < 1 or n > MechanicalParameters.PCR_tray_count_rows):
            return None
        self.printer_handle.moveZRelative(MechanicalParameters.PCR_tray_distance_tip_inserted_mm * -1)
        if offset == None:
            # No Offset Required. Go To Center Of The Well
            self.printer_handle.moveYAbsolute(self.__get_row_n(n))
        elif offset == True:
            # Offset Required
            self.printer_handle.moveYAbsolute(
                self.__get_row_n(n) + MechanicalParameters.PCR_tray_offset_from_center_mm)
        self.printer_handle.moveZAbsolute(MechanicalParameters.PCR_tray_distance_coasting_with_tip_mm + \
                                          MechanicalParameters.PCR_tray_distance_tip_inserted_mm)
