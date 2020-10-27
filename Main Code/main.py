#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import time
import sys
import subprocess
import os
from datetime import datetime
import faulthandler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from threads.Printer import Printer
from classes.MainUI import MainUI
from classes.Tests import Tests
from classes.Buzzer import Buzzer
from classes.DeviceConfig import DeviceConfig
from helpers.BaseLogger import BaseLogger

# Global Variables
device_config = None
tests = None
main_app = None
main_window = None
thread_printer = None

path_config_file_system = '/home/pi/xenovia/config/config_system.yaml'
path_config_file_test = '/home/pi/xenovia/config/config_tests.yaml'

if __name__ == '__main__':

    faulthandler.enable()

    #Start GUI Subsystem
    BaseLogger.info('Starting GUI ...')
    main_app = QtWidgets.QApplication(sys.argv)
    main_window = MainUI()

    # Read Device Configuration
    BaseLogger.info('Reading device configuration')
    device_config = DeviceConfig(config_file_path=path_config_file_system)

    # Print Firmware Info
    BaseLogger.info('---------------------------')
    BaseLogger.info(device_config.deviceName)
    BaseLogger.info('ver : ' + device_config.deviceFirmware)
    BaseLogger.info('date : ' + device_config.deviceFirmwareDate)
    BaseLogger.info('---------------------------')

    # Read Tests
    BaseLogger.info('Populating available tests')
    tests = Tests(test_file_path=path_config_file_test)

    # Initialize Printer
    thread_printer = Printer(main_window)
    thread_printer.start()
       
    main_window.setHandlePrinter(thread_printer)
    main_window.setHandleTests(tests)
sys.exit(main_app.exec_())