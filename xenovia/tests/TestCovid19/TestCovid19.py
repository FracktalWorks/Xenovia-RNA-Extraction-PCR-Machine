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
            # Tip Row number 1
        'self.imagebox_signal.emit("image1.png")',
        'self.textbox_signal.emit("test started")',
        'self.imagebox_signal.emit("image2.png")',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(3)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(10.00)',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',
        
        # Tip Row number 2
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(3)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(2)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(10.00)',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 3
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(10)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(11)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(10.00)',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 4
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(10)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(12)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(10.00)',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()'
        'self.pipette.dispense()',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',

        # Tip Row number 5
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(4)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 6
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(4)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(2)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 7
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(9)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(11)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 8
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(9)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(12)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 9
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(4)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(6)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.well.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 5, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.pcr.gotoRowN(1)',
        'self.pipette.dispense()',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 10
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(4)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(2)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(6)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.well.gotoRowN(2)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 5, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.pcr.gotoRowN(2)',
        'self.pipette.dispense()',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 11
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(9)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(11)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(7)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.well.gotoRowN(11)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 5, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.pcr.gotoRowN(3)',
        'self.pipette.dispense()',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        # Tip Row number 12
         'self.tip_holder.getTips()',
        'self.well.gotoRowN(9)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.well.gotoRowN(12)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 10, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(7)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.well.gotoRowN(12)',
        'self.pipette.dispense()',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_100, 5, 1, 1)',
        'self.magnet.engageAll()',
        'self.holdTestMinutes(1.00)',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_50)',
        'self.pcr.gotoRowN(4)',
        'self.pipette.dispense()',
        'self.tip_trash.trashTips()',
        'self.magnet.disengageAll()',

    ]

    def __init__(self, printer=None, \
                        tip_holder=None, \
                        well=None, \
                        pcr=None,\
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
            pcr,\
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
