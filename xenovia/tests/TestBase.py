#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: June 2020
 *
 * Base Class For Test
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from classes.Pipette import Pipette
from helpers.BaseLogger import BaseLogger

class TestBase(QtCore.QThread):
    printer = None
    tip_holder = None
    well = None
    tip_trash = None
    pipette = None
    magnet = None
    imagebox_signal = None
    textbox_signal = None
    progressbar_signal = None
    aborted_signal = None
    finished_signal = None
    timer = None

    test_step_current = 0
    test_step_minor = 0
    test_step_major = 0
    test_progress_delta = 0
    test_progress_current = 0
    test_aborting = False
    test_aborted = False

    def __init__(self, printer, tip_holder, well, tip_trash, pipette, magnet, imagebox_signal, textbox_signal, progressbar_signal, test_abort_signal, test_finish_signal):
        if not printer \
            or not tip_holder \
            or not well \
            or not tip_trash \
            or not pipette \
            or not magnet \
            or not imagebox_signal \
            or not textbox_signal \
            or not progressbar_signal \
            or not test_abort_signal \
            or not test_finish_signal:
            raise TypeError('required arguments missing')
        super(TestBase, self).__init__()
        self.printer = printer
        self.tip_holder = tip_holder
        self.well = well
        self.tip_trash = tip_trash
        self.pipette = pipette
        self.magnet = magnet
        self.imagebox_signal = imagebox_signal
        self.textbox_signal = textbox_signal
        self.progressbar_signal = progressbar_signal
        self.aborted_signal = test_abort_signal
        self.finished_signal = test_finish_signal
        BaseLogger.info('Test Initialized')
    
    def parseTest(self, test_steps=None):
        # Parse Test And Update Test Metrics
        self.test_step_major = 0
        self.test_step_minor = 0
        if not test_steps:
            raise TypeError('required arguments missing')
        for i in test_steps:
            if not i.startswith('self.imagebox_signal') and not i.startswith('self.textbox_signal'):
                # This Is A Major Test Step
                self.test_step_major += 1
            else:
                # This Is A Minor  Test Step
                self.test_step_minor += 1
        self.test_progress_delta = 100 / self.test_step_major
        BaseLogger.info('Test step total = ' + str(self.test_step_major + self.test_step_minor))
        BaseLogger.info('Test step major = ' + str(self.test_step_major))
        BaseLogger.info('Test step minor = ' + str(self.test_step_minor))
        BaseLogger.info('Test progress delta = ' + str(self.test_progress_delta))
    
    def isTestStepMajor(self, step):
        # Check If Test Step Is Major
        if not step.startswith('self.imagebox_signal') and not step.startswith('self.textbox_signal'):
            return True
    
    def holdTestSeconds(self, delay_sec=None):
        # Delay / Sleep Test For delay_sec Seconds
        if not delay_sec:
            raise TypeError('required arguments missing')
        time.sleep(delay_sec)

    def holdTestMinutes(self, delay_min=None):
        # Delay / Sleep Test For delay_min Minutes
        if not delay_min:
            raise TypeError('required arguments missing')
        time.sleep(delay_min * 60)
    
    def setupTest(self):
        # Setup Test
        self.test_step_current = 1
        self.test_step_major_current = 1
        self.test_progress_current = 0
        self.progressbar_signal.emit(self.test_progress_current)
        BaseLogger.info('Test Started')

    def runTest(self, test_steps):
        # Run Test
        self.tip_holder.reset()
        self.pipette.dispense()
        if not test_steps:
            raise TypeError('required arguments missing')
        for step in test_steps:
            BaseLogger.info('Test step (' + str(self.test_step_current)+ '/' + str(self.test_step_major + self.test_step_minor) + ')')
            exec(step)
            if bool(self.isTestStepMajor(step)):
                self.test_progress_current = self.test_progress_delta * self.test_step_major_current
                self.test_step_major_current += 1
                self.progressbar_signal.emit(self.test_progress_current)
            self.test_step_current += 1
            # Check For Test Abort
            if(self.test_aborting):
                self.printer.home()
                self.test_aborted = True
                BaseLogger.info('Test aborted')
                self.aborted_signal.emit()
                return
        BaseLogger.info('Test Finished')
        self.finished_signal.emit()

    def abortTest(self):
        # Initiate Test Abort
        self.test_aborting = True
        BaseLogger.info('Test aborting')

    def aborted(self):
        # Return Test Aborted Status
        return self.test_aborted