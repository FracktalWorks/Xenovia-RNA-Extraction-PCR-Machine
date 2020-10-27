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


class colorSensorArray(object):
    '''
    Main class object for color sensor
    :param i2cbus (int):                The i2c bus the device is connected on
    :param sensorChannels (list[int]):  list of sensor channels connected.
                                        if single int given, it is converted to a list
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
        :returns bool:          result of hardware check. True if all ok, False if it isnt
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
        :returns bool:          True if all hardware connected, false if not
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
        """
        Gets value of CONF register of each sensor channel
        :param channels (list[int]):            List of channels to get CONF register value from.
                                                if int provided, it is converted to list
        :returns values (list):                 list of CONF register values for sensor channels
        """
        values = []
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            values.append(self.colorSensor.getCONF())
            self.mux.disableChannels(channel)
        return values


    def enableSensor(self,channels = None):
        """
        Enables the channels of the color sensor array
        :param channels (list[int]):            List of channels to enable sensor on
                                                if int provided, it is converted to list
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            self.colorSensor.enableSensor()
            self.mux.disableChannels(channel)

    def dissableSensor(self,channels = None):
        """
        Enables the channels of the color sensor array
        :param channels (list[int]):            List of channels to disable sensor on
                                                if int provided, it is converted to list
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            self.colorSensor.disableSensor()
            self.mux.disableChannels(channel)

    def setSensorIT(self,it=2,channels = None):
        """
        Sets integration time for all sensors in array
        :param it (int):          Integration time

        IT   INTEGRATION TIME   G SENSITIVITY       MAX. DETECTABLE LUX
        0    40 ms               0.25168             16 496
        1    80 ms               0.12584             8248
        2    160 ms              0.06292             4124
        3    320 ms              0.03146             2062
        4    640 ms              0.01573             1031
        5    1280 ms             0.007865            515.4

        :param channels (list[int]):            List of channels to set IT on
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            self.colorSensor.setIT(it)
            self.mux.disableChannels(channel)

    def setSensorMode(self,auto=True, channels = None):
        """
        sets mode for all sensors in array to triggered (Manual Force Mode) or auto Mode
        :param channels (list[int]):            List of channels to set IT on
        :param auto (bool):                     flag to set reading mode.
                                                True = Auto Mode
                                                False = Manual Force MOde
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        if auto:
            for channel in channels:
                if channel not in self.sensorChannels:
                    raise ValueError("Sensor channels provided are not available")
                self.mux.enableChannels(channel)
                self.colorSensor.autoMode()
                self.mux.disableChannels(channel)
        else:
            for channel in channels:
                if channel not in self.sensorChannels:
                    raise ValueError("Sensor channels provided are not available")
                self.mux.enableChannels(channel)
                self.colorSensor.forceMode()
                self.mux.disableChannels(channel)

    def channelTrigger(self,channels = None):
        """
        Triggers one detection cycle for sensor channel(s) when in manual force mode
        :param channels (list[int]):            List of channels to trigger sensing
        """
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            self.colorSensor.trigger()
            self.mux.disableChannels(channel)

    def readRGBW(self,channels = None):
        """
        Reads all colors from channels of the sensor
        :param channels (list[int]):            List of channels to read values from
        """
        values = []
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
            self.mux.enableChannels(channel)
            values.append(self.colorSensor.getRGBW())
            self.mux.disableChannels(channel)
        return values

    def readColors(self,color = ["red","green","blue","white"], channels = None):
        """
        reads specific colors from the channels of the sensor
        :param color (list[str]):           list of colors needed to be read from each sensor
        :param channels (list[int]):            List of channels to read values from
        """
        if type(color) is not list: color = [color]
        values = []
        self.mux.disableAll()
        if channels == None:
            channels = self.sensorChannels
        if type(channels) is not list: channels = [channels]
        for channel in channels:
            if channel not in self.sensorChannels:
                raise ValueError("Sensor channels provided are not available")
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