#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Device Configuration Class
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import yaml

from helpers.BaseLogger import BaseLogger

class DeviceConfig:
    #Device Configuration Class
    def __init__(self, config_file_path):
        self.configFilePath = config_file_path
        with open(self.configFilePath, 'r') as ymlfile:
            try:
                self.configData = yaml.safe_load(ymlfile)
                self.isConfigPresent = True
                self.deviceName = self.configData.get('info_device').get('name')
                self.deviceFirmware = str(self.configData.get('info_release').get('version_major')) + '.' + str(self.configData.get('info_release').get('version_minor'))
                self.deviceFirmwareDate = self.configData.get('info_release').get('date')
            except yaml.YAMLError as error:
                self.isConfigPresent = False
                self.deviceName = ''
                self.deviceFirmware = ''
                self.deviceFirmwareDate = ''
                self.octoprintServerIP = ''
                self.octoprintAPIKey = ''
                BaseLogger.error(error)