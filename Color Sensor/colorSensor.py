#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  colorSensor.py
#  library for Fracktal Xenovia Color Sensor
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
#  Written by vjvarada (Vijay Raghav Varada)

import smbus
import time
from veml6040 import VEML6040
from tca9548a import TCA9548A
import threading


class colorSensor(object):
    '''
    Main class object for color sensor
    '''

    def __init__(self, i2cBus = None,sensorChannels = None):
        if i2cBus == None:
            i2c = smbus.SMBus(1)
        else:
            i2c = smbus.SMBus(i2cBus)
        self.mux = TCA9548A(0x70,None,i2c,None,11)
        self.colorSensor = VEML6040(i2c,None)
        if sensorChannels == None:
            self.sensorChannels = [0,1,2,3,4,5,6,7]
        elif type(sensorChannels) is not list:
            self.sensorChannels = [sensorChannels]
        else:
            self.sensorChannels = sensorChannels


    def hardwareCheck(self):
        """
        Check if all hardware is functioning fine
        """
        if self.mux.isConnected() == False:
            print "TCA9458A is Not Connected"
            return False
        else:
            print "TCA9458A is Connected"
        self.mux.disableAll()
        for sensor in self.sensorChannels:
            self.mux.enableChannels(sensor)
            if self.colorSensor.isConnected():
                print "Color Sensor detected on channel: " + str(sensor)
            else:
                print "Color Sensor error on channel: " + str(sensor)
            self.mux.disableChannels(sensor)
        if sensor == 7:
            print "All hardware is connected"
            return True
        else:
            print "Hardware Malfunction, check sensor connections"
            return False

    def isConnected(self):
        """
        Check if all hardware is functioning fine
        """
        if self.mux.isConnected() == False:
            return False
        self.mux.disableAll()
        for channel in self.sensorChannels:
            self.mux.enableChannels(channel)
            if self.colorSensor.isConnected():
                self.mux.disableChannels(channel)
            else:
                return False
            return True

    def getCONF(self,channels = None):
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            print "Sensor on channel " + str(channel) + ", CONF: " + str(self.colorSensor.getCONF())
            self.mux.disableChannels(channel)


    def enableSensor(self,channels = None):
        """
        Enables a single sensor and mux channel
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            self.colorSensor.enableSensor()
            self.mux.disableChannels(channel)

    def dissableSensor(self,channels):
        """
        dissables all sensors and mux channels
        """
        self.mux.disableAll()
        for channel in channels:
            self.mux.enableChannels(channel)
            self.colorSensor.disableSensor()
            self.mux.disableChannels(channel)

    def setSensorIT(self,it=2,channels = None):
        """
        Sets integration time for all sensors in array
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            self.colorSensor.setIT(it)
            self.mux.disableChannels(channel)

    def setSensorMode(self,channels = None,auto=True):
        """
        sets mode for all sensors in array to triggered (Manual Force Mode) or auto Mode
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        if auto:
            for channel in channels:
                self.mux.enableChannels(channel)
                self.colorSensor.autoMode()
                self.mux.disableChannels(channel)
        else:
            for channel in channels:
                self.mux.enableChannels(channel)
                self.colorSensor.forceMode()
                self.mux.disableChannels(channel)

    def channelTrigger(self,channels = None):
        "triggers one detection cycle for sensor channel(s) when in manual force mode"
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            self.colorSensor.trigger()
            self.mux.disableChannels(channel)

    def readRGBW(self,channels = None):
        "reads channels from the sensor"
        values = []
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            values.append(self.colorSensor.getRGBW())
            self.mux.disableChannels(channel)
        return values

    def readColors(self,color = ["red","green","blue","white"], channels = None):
        "reads channels from the sensor"
        if type(color) is not list: color = [color]
        values = []
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            self.mux.enableChannels(channel)
            value = []
            if "red" in color:
                value.append(self.colorSensor.getRed())
            if "green" in color:
                value.append(self.colorSensor.getGreen())
            if "blue" in color:
                value.append(self.colorSensor.getBlue())
            if "white" in color:
                value.append(self.colorSensor.getWhite())
            self.mux.disableChannels(channel)
            values.append(value)
        return values


def main(args):
    Sensor = colorSensor()
    Sensor.hardwareCheck()
    Sensor.setSensorMode(None,auto=True)
    Sensor.getCONF()
    if Sensor.isConnected():
        Sensor.enableSensor()
        Sensor.setSensorIT(2)
        print Sensor.readColors(color = "green")

###########################

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
