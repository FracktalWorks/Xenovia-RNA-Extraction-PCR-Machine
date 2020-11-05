#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: July 2020
 *
 * Machine Mechanical Parameters Class
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

class MechanicalParameters(object):
    # Class To Specify The Mechanical Parameters Of The Machine 
    # Which Are Then Referrenced By Other Firmware Classes
    # ********* WARNING !!!! **********
    # ********* DO NOT MODIFY *********

    # Magnet
    # 2 Servos
    servo_ports = [0, 1]
    servo_position_degree_disengaged = [0, 0]
    servo_position_degree_engaged = [90, 90]

    # Pipette
    # 4 Predefined Liquid Levels
    pipette_level_count = 4
    pipette_distance_aspirate_max_mm = 19
    pipette_distance_aspirate_min_mm = [11, 9, 6, 4]

    # Tip
    tip_length_mm = 57

    # Tip Holder Tray
    tip_tray_count_rows = 12
    tip_tray_count_columns = 8
    tip_tray_position_origin_mm = 2.1
    tip_tray_offset_row1_origin_mm = 10
    tip_tray_offset_inter_row_mm = 9
    tip_tray_distance_coasting_without_tip_mm = 58
    tip_tray_distance_coasting_with_tip_mm = tip_tray_distance_coasting_without_tip_mm - tip_length_mm
    tip_tray_distance_pipette_tip_lock_mm = 71 #103

    # Tip Trash
    tip_trash_position_origin_mm = 375
    tip_trash_position_groove_mm = tip_trash_position_origin_mm + 22
    tip_trash_offset_tip_groove_size_mm = 6
    tip_trash_distance_coasting_without_tip_mm = 20
    tip_trash_distance_coasting_with_tip_mm = tip_trash_distance_coasting_without_tip_mm - tip_length_mm
    tip_trash_distance_tip_groove_locking_mm = 20
    tip_trash_distance_tip_groove_unlocking_mm = 10

    # Well Tray
    well_tray_count_rows = 12
    well_tray_count_columns = 8
    well_tray_position_origin_mm = 146.50 #194
    well_tray_offset_row1_origin_mm = 10
    well_tray_offset_inter_row_mm = 9
    well_tray_offset_from_center_mm = 2.5
    well_tray_distance_tip_inserted_mm = 30
    well_tray_distance_coasting_without_tip_mm = 22
    well_tray_distance_coasting_with_tip_mm = well_tray_distance_coasting_without_tip_mm - tip_length_mm

    # PCR Tray
    PCR_tray_count_rows = 4
    PCR_tray_count_columns = 8
    PCR_tray_position_origin_mm = 20
    PCR_tray_offset_row1_origin_mm = 3
    PCR_tray_offset_inter_row_mm = 9
    PCR_tray_offset_from_center_mm = 2.5
    PCR_tray_distance_tip_inserted_mm = 30
    PCR_tray_distance_coasting_without_tip_mm = 90
    PCR_tray_distance_coasting_with_tip_mm = PCR_tray_distance_coasting_without_tip_mm - tip_length_mm

    def __init__(self):
        pass
