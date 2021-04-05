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
    servo_position_degree_disengaged = [0, 0]#[100, 100]
    servo_position_degree_engaged = [130, 130]#[125, 125]#[135, 150]#[0, 0]

    # Pipette
    # 4 Predefined Liquid Levels
    pipette_level_count = 4
    pipette_distance_aspirate_max_mm = 19
    pipette_distance_aspirate_min_mm = [16.66, 13.33, 5.66, 0] #[11, 9, 6, 4]

    # Tip
    tip_length_mm = 57

    # Tip Holder Tray
    tip_tray_count_rows = 12
    tip_tray_count_columns = 8
    tip_tray_position_origin_mm = 6.8#6.4
    tip_tray_offset_row1_origin_mm = 10
    tip_tray_offset_inter_row_mm = 9
    tip_tray_distance_coasting_without_tip_mm = 40
    tip_tray_distance_coasting_with_tip_mm = tip_tray_distance_coasting_without_tip_mm - tip_length_mm
    tip_tray_distance_pipette_tip_lock_mm = 66.5 #103

    # Tip Trash
    tip_trash_position_origin_mm = 344.8 #365
    tip_trash_position_groove_mm = tip_trash_position_origin_mm + 57#32
    tip_trash_offset_tip_groove_size_mm = 55 #30
    tip_trash_distance_coasting_without_tip_mm = 80
    tip_trash_distance_coasting_with_tip_mm = 19 #23 #tip_trash_distance_coasting_without_tip_mm - tip_length_mm
    tip_trash_distance_tip_groove_locking_mm = 10
    tip_trash_distance_tip_groove_unlocking_mm = 12#15#14

    # Well Tray
    well_tray_count_rows = 12
    well_tray_count_columns = 8
    well_tray_position_origin_mm = 149.8#149.4#153.1 #194
    well_tray_offset_row1_origin_mm = 10
    well_tray_offset_inter_row_mm = 9
    well_tray_offset_from_center_mm = 1#3#4#2.5
    well_tray_distance_tip_inserted_mm = 33.5#32#31#29#30 #40 #33.2
    well_tray_distance_coasting_without_tip_mm = 75#80 #70 #20
    well_tray_distance_coasting_with_tip_mm = well_tray_distance_coasting_without_tip_mm - tip_length_mm

    # PCR Tray
    PCR_tray_count_rows = 4
    PCR_tray_count_columns = 8
    PCR_tray_position_origin_mm = 292
    PCR_tray_offset_row1_origin_mm = 4
    PCR_tray_offset_inter_row_mm = 9
    PCR_tray_offset_from_center_mm = 2.5
    PCR_tray_distance_tip_inserted_mm = 30
    PCR_tray_distance_coasting_without_tip_mm = 80
    PCR_tray_distance_coasting_with_tip_mm = PCR_tray_distance_coasting_without_tip_mm - tip_length_mm

    def __init__(self):
        pass
