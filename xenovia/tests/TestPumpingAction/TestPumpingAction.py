#!/usr/bin/python

'''
*************************************************************************
 * TEST   : PUMPING ACTION
 * DATE   : 21/6/2020
 * AUTHOR : ANKIT BHATNAGAR
*************************************************************************
'''

import time

from tests.TestBase import TestBase
from helpers.BaseLogger import BaseLogger

class TestPumpingAction(TestBase):
    # Test Specific Data
    test_steps  = [
              
     # Tip Row number 1
        'self.imagebox_signal.emit("image1.png")',
        'self.textbox_signal.emit("test started")',
        'self.imagebox_signal.emit("image2.png")',
        'self.magnet.disengageAll()',
        'self.tip_holder.getTips()',
        'self.well.gotoRowN(1)',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 5, 1, 1)',#10times not 5
        'self.tip_trash.moveUp()',

        'self.well.gotoRowN(2)',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 5, 1, 1)',#10times not 5
        'self.tip_trash.moveUp()',

        'self.well.gotoRowN(11)',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 5, 1, 1)',#10times not 5
        'self.tip_trash.moveUp()',

        'self.well.gotoRowN(12)',
        'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 5, 1, 1)',#10times not 5
        'self.tip_trash.moveUp()',
        ##'self.tip_trash.trashTips()',
        ##'self.pipette.dispense()',
        ##'self.tip_trash.moveToTrashUnlock()',
        #'self.holdTestMinutes(10.00)',#10min not 1
        ##'self.tip_holder.getTips()',
        ##'self.well.gotoRowN(12)',
        ##'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 10, 1, 1)',#10times not 5
        ##'self.pipette.dispense()',
        ##'self.tip_trash.moveUp()',
        #'self.tip_trash.trashTips()',
        #'self.tip_trash.moveToTrashUnlock()',
        #'self.tip_holder.getTips()',
        #'self.holdTestMinutes(10.00)',#10min not 1
        'self.magnet.engageAll()',

        'self.holdTestMinutes(1.00)',
        ##'self.well.gotoRowN(12)',
        ##'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 2, 1, 1)',#10times not 5
        ##'self.pipette.dispense()',
        ##'self.tip_trash.moveUp()',
        ##'self.tip_trash.trashTips()',
        ##'self.tip_trash.moveToTrashUnlock()',
        ##'self.tip_holder.getTips()',
        #'self.well.gotoRowN(1)',
        #'self.pipette.pump(Pipette.PIPETTE_LEVEL_UL_300, 2, 1, 1)',#10times not 5
        #'self.magnet.engageAll()',
        #'self.pipette.dispense()',
        #'self.tip_trash.moveUp()',
        #'self.tip_trash.trashTips()',
        #'self.tip_trash.moveToTrashUnlock()',
        #'self.tip_holder.getTips()',
        #'self.magnet.engageAll()',
        #'self.holdTestMinutes(1.00)',
        
        #Dispense 470 at trash with tips at end
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',
        'self.well.gotoRowN(1)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',
        'self.well.gotoRowN(2)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',
        'self.well.gotoRowN(11)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',

        'self.tip_holder.getTips()',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_300)',
        'self.tip_trash.moveToTrash()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',
        'self.well.gotoRowN(12)',
        'self.pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_170)',
        'self.tip_trash.trashTips()',
        'self.pipette.dispense()',
        'self.tip_trash.moveToTrashUnlock()',  

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
