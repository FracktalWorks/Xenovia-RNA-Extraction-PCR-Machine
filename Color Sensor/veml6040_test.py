#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  VEML6040.py
#
#  Copyright 2020  <pi@kb>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Written by BitHead (Britany Head)
# Step 1) Enable I2C in Raspi-Config (Interfacing Options)
# Step 2) sudo apt-get install i2c-tools python3-smbus
# Step 3) plug it in (don't forget your pull-up resistors) and run this program

import smbus
import time
import threading

bus = smbus.SMBus(1)  # /dev/i2c-1, in my case


class VEML6040(object):

    def __init__(self, i2c_driver=None,bus=None,resetPin = None):
        """
                This method initializes the class object. If no 'address' or
                'i2c_driver' are inputed or 'None' is specified, the method will
                use the defaults.
                :param address: 	The I2C address to use for the device.
                                    If not provided, the method will default to
                                    the 0x10
                :param i2c_driver:	An existing SMBus driver object.If not parsed, it is created
                :param bus:         bus number of i2c bus on rpi. Defaults to 1 is nothing passed
                """
        self.VEML6040_ADDR = 0x10 #default i2c address of
        self.VEML6040_CONF = 0x00 #address of CONF register for operation control and parameter setup

        # Load the I2C driver if one isn't provided
        if i2c_driver == None:
            if bus == None:
                self._i2c = smbus.SMBus(1)
            else:
                self._i2c = smbus.SMBus(bus)

            if self._i2c == None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

    def is_connected(self):
        """
            Determine if the device is conntected to the system.
            :return: True if the device is connected, otherwise False.
            :rtype: bool
        """
        try:
            print self.read(self.VEML6040_CONF)
            time.sleep(.001)
            return True
        except IOError:
            return False

    # -------------------------
    def write(self,cmd, val):  # //Write 0x00 register
        self._i2c.write_word_data(self.VEML6040_ADDR, cmd, val)


    # -------------------------
    def read(self,cmd):
        return self._i2c.read_word_data(self.VEML6040_ADDR, cmd)


    # -------------------------
    def getRed(self):  # //Get red light measurement
        return self.read(0x08);


    # -------------------------
    def getGreen(self):  # //Get green light measurement
        return self.read(0x09);


    # -------------------------
    def getBlue(self):  # //Get blue light measurement
        return self.read(0x0A);


    # -------------------------
    def getWhite(self):  # //Get white light measurement
        return self.read(0x0B)


    # -------------------------
    def enableSensor(self):  # //Enable light sensor in VEML6040
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x00FE
        self.write(self.VEML6040_CONF, conf)
        time.sleep(.001)


    # -------------------------
    def disableSensor(self):  # //Disable light sensor
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x00FE
        conf = conf | 0x000
        self.write(self.VEML6040_CONF, conf)
        time.sleep(.001)


    # -------------------------
    def setIT(self,it):  # integration time  0=40ms,1=80,2=160,3=320,4=640,5=1280ms
        conf =self. read(self.VEML6040_CONF)
        conf = conf & 0x0003
        it = it << 4
        self.write(self.VEML6040_CONF, (conf | it))


    # -------------------------
    def forceMode(self):  # forced measurement mode.(Trigger to start)
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0072
        conf = conf | 0x0002
        self.write(self.VEML6040_CONF, conf)


    # -------------------------
    def autoMode(self):  # auto measurement mode
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0070
        self.write(self.VEML6040_CONF, conf)


    # -------------------------
    def trigger(self):  # Trigger a measurement (forced mode)
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0072
        self.write(self.VEML6040_CONF, (conf | 0x0004))
        time.sleep(.001)
        self.write(self.VEML6040_CONF, (conf & 0x0070))

    def map(self,val,in_min,in_max,out_min,out_max):
        return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def readAllLoop(self):
        # r = getRed()
        # g = getGreen()
        # b = getBlue()  # just a little balancing act
        # w = getWhite()
        r = self.map(self.getRed(),0,4124,0,254)
        g = self.map(self.getGreen(),0,4124,0,254)
        b = self.map(self.getBlue(),0,4124,0,254)  # just a little balancing act
        w = self.map(self.getWhite(),0,4124,0,254)
        kMax = r
        klr = "red"
        if (g > kMax):
            kMax = g
            klr = "green"
        if (b > kMax): klr = "blue"

        print("red=", r, " : ", "grn=", g, " : ", "blu=", b, " : ", "wht=", w, "  Winner is", klr)
        loopTimer = threading.Timer(0.5, self.readAllLoop)
        loopTimer.start()




#######################################################################

def main(args):
    colorSesnor = VEML6040()
    print colorSesnor.is_connected()
    colorSesnor.enableSensor()
    colorSesnor.setIT(2)
    colorSesnor.autoMode()
    colorSesnor.readAllLoop()
    return 0


###########################

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
