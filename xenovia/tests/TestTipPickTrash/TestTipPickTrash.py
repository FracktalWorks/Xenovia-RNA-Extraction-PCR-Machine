#!/usr/bin/python

'''
*************************************************************************
 * TEST   : TIP PICK TRASH
 * DATE   : 21/6/2020
 * AUTHOR : ANKIT BHATNAGAR
*************************************************************************
'''

import time

from tests.TestBase import TestBase
from helpers.BaseLogger import BaseLogger

class TestTipPickTrash(TestBase):
    # Test Specific Data
    test_steps  = [
        'self.imagebox_signal.emit("image1.png")',
        'self.textbox_signal.emit("test started")',
        'self.imagebox_signal.emit("image2.png")',
        'self.tip_holder.getTips()',
        'self.tip_trash.trashTips()'       
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