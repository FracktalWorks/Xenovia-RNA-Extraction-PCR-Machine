#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  veml6040.py
#  Vishay Semiconductor VEML6040 Python Library
#
#  Copyright 2020  Fracktal Works
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
#  Written by @vjvarada (Vijay Raghav Varada)

import smbus
import time

class VEML6040(object):

    def __init__(self, i2c_driver=None,bus=None):
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

    def isConnected(self):
        """
            Determine if the device is conntected to the system.
            :return: True if the device is connected, otherwise False.
            :rtype: bool
        """
        try:
            self.read(self.VEML6040_CONF)
            return True
        except IOError:
            return False

    def getCONF(self):
        """
        Reads the CONF register of the sensor
        returns:        int CONF register value
        """
        return self.read(self.VEML6040_CONF)


    def write(self,cmd, val):
        """
        Writes a value to the devices register
        :param cmd:         Register to write to
        :param val:         Value to write to the register

        """
        self._i2c.write_word_data(self.VEML6040_ADDR, cmd, val)

    def read(self,cmd):
        """
        Reads a value from the register
        :param cmd:         Register to read

        """
        return self._i2c.read_word_data(self.VEML6040_ADDR, cmd)


    def getRed(self):
        """
        Gets value of red component of light
        :returns:           16 bit LUX value of red
        """
        return self.read(0x08);

    def getGreen(self):
        """
        Gets value of green component of light
        :returns:           16 bit LUX value of green
        """
        return self.read(0x09);

    def getBlue(self):
        """
        Gets value of blue component of light
        :returns:           16 bit LUX value of blue
        """
        return self.read(0x0A);

    def getWhite(self):
        """
        Gets value of white
        :returns:           16 bit LUX value of white
        """
        return self.read(0x0B)

    def getRGBW(self):
        return [self.getRed(),self.getGreen(),self.getBlue(),self.getWhite()]

    def enableSensor(self):
        """
        Enables the light sensor by setting the SD bit of the CONF register
        """
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x00FE
        self.write(self.VEML6040_CONF, conf)
        time.sleep(.001)

    def disableSensor(self):
        """
        Dissables the light sensor by setting the SD bit of the CONF register
        """
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x00FE
        conf = conf | 0x000
        self.write(self.VEML6040_CONF, conf)
        time.sleep(.001)

    def setIT(self,it):  # integration time  0=40ms,1=80,2=160,3=320,4=640,5=1280ms
        """
        Sets the integration time, thereby changing the channel resolution and maximum detection range
        :param it:          Integration time

        IT   INTEGRATION TIME   G SENSITIVITY       MAX. DETECTABLE LUX
        0    40 ms               0.25168             16 496
        1    80 ms               0.12584             8248
        2    160 ms              0.06292             4124
        3    320 ms              0.03146             2062
        4    640 ms              0.01573             1031
        5    1280 ms             0.007865            515.4
        """
        conf =self. read(self.VEML6040_CONF)
        conf = conf & 0x0003
        it = it << 4
        self.write(self.VEML6040_CONF, (conf | it))

    def forceMode(self):
        """
        Sets sensor to manual force mode, needing trigger() to start
        """
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0072
        conf = conf | 0x0002
        self.write(self.VEML6040_CONF, conf)

    def autoMode(self):
        """
        Sets sensor to Auto mode, read LUX registers directly without triggering
        """
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0070
        self.write(self.VEML6040_CONF, conf)

    def trigger(self):
        """
        Trigger a measurement in manual forced mode
        """
        conf = self.read(self.VEML6040_CONF)
        conf = conf & 0x0072
        self.write(self.VEML6040_CONF, (conf | 0x0004))
        time.sleep(.001)
        self.write(self.VEML6040_CONF, (conf & 0x0070))
