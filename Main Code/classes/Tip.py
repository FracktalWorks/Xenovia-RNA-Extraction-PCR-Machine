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

from classes.MechanicalParameters import MechanicalParameters;
from helpers.BaseLogger import BaseLogger

class Tip:
    # Class To Hold Tip Holder Positional And Dimensional Parameters
    # All Distances From Printer Home
    
    # Mechanical Parameters 
    height_tip_mm = MechanicalParameters.tip_length_mm