#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * MKS Connection Check Thread
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import time
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from helpers.BaseLogger import BaseLogger
from helpers.USB import *

class MKSCheck(QtCore.QThread):
    # Thread For Checking MKS Board 1.4 Connection
    # MKS USB Serial Connection Configure On File /dev/makerbase
    # /etc/udev/rules.d/99-usb-serial.rules

    signal = pyqtSignal(str)

    def __init__(self):
        super(MKSCheck, self).__init__()
        self.connected = False
        self.probe_time = 0
        self.mks_port = None     

    def getStatus(self):
        # Return MKS Connection Status
        return self.connected

    def getPort(self):
        # Return MKS Serial Port Identifier
        return self.mks_port

    def run(self):
        # Find Which Port MKS Is On
        self.mks_port = USBIdentifyFTDIPort()
        if(self.mks_port is None):
            BaseLogger.info('MKS - cannot find port')
            self.signal.emit('MKS-FAIL')
            return
        BaseLogger.info('MKS PORT : ' + self.mks_port)
        self.connected = True
        self.signal.emit('MKS-OK')