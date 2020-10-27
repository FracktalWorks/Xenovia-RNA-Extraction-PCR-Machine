#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * USB Helper Functions
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
import subprocess

def USBIdentifyFTDIPort():
    # Return USB Port Path Where FTDI USB-SERIAL
    # Chip Is Detected
    result = subprocess.run('dmesg | grep "ttyUSB"', capture_output=True, shell=True, encoding='utf8')
    result = result.stdout.split('\n')
    result = [s.strip() for s in result]
    for line in result:
        if 'FTDI' in line:
            port = line[line.index('ttyUSB'):line.index('ttyUSB') + 7]
            return '/dev/' + port
    return None
