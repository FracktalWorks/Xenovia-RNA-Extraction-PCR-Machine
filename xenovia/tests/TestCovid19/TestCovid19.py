#!/usr/bin/python

'''
*************************************************************************
 * TEST   : COVID-19
 * DATE   : 9/6/2020
 * AUTHOR : ANKIT BHATNAGAR
*************************************************************************
'''

import time
from classes.Pipette import Pipette
from tests.TestBase import TestBase
from helpers.BaseLogger import BaseLogger

class TestCovid19(TestBase):
    # Test Specific Data
    test_steps  = [
        'self.imagebox_signal.emit("image1.png")',
        'self.textbox_signal.emit("test started")',
        'self.imagebox_signal.emit("image2.png")',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.holdTestMinutes(0.2)',
        'self.magnet.engageAll()',
        'self.tip_holder.getTips()',
        'self.holdTestMinutes(0.2)',
        'self.well.gotoRowN(1, True)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(3)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.holdTestMinutes(0.2)',
        'self.magnet.engageAll()',
        'self.tip_holder.getTips()',
        'self.holdTestMinutes(0.2)',
        'self.well.gotoRowN(1, True)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(4)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.holdTestMinutes(0.2)',
        'self.magnet.engageAll()',
        'self.tip_holder.getTips()',
        'self.holdTestMinutes(0.2)',
        'self.well.gotoRowN(1, True)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
        'self.holdTestMinutes(0.05)',
	'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(5)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
	'self.holdTestMinutes(0.05)',
        'self.tip_trash.trashTips()',
        'self.holdTestMinutes(0.2)',
        'self.magnet.engageAll()',
        'self.tip_holder.getTips()',
        'self.holdTestMinutes(0.2)',
        'self.well.gotoRowN(1, True)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_100)',
	'self.holdTestMinutes(0.05)',
        'self.well.gotoRowN(6)',
        'self.pipette.dispense()',
        'self.magnet.disengageAll()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
	'self.holdTestMinutes(0.05)',
        'self.pipette.dispense()',
        'self.tip_trash.trashTips()',
    ]

    def __init__(self, printer=None, \
                        tip_holder=None, \
                        well=None, \
                        tip_trash=None, \
                        pipette = None, \
                        magnet = None, \
                        imagebox_signal=None, \
                        textbox_signal=None, \
                        progressbar_signal=None, \
                        abort_signal=None, \
                        finish_signal=None):
        TestBase.__init__(self, \
            printer, \
            tip_holder, \
            well, \
            tip_trash, \
            pipette, \
            magnet, \
            imagebox_signal, \
            textbox_signal, \
            progressbar_signal, \
            abort_signal, \
            finish_signal)
        self.parseTest(self.test_steps)

    def run(self):
        self.setupTest()
        self.runTest(self.test_steps)
