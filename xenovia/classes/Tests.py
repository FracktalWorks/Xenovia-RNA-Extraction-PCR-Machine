#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Class To Manage Available Tests
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
import yaml
import importlib

from helpers.BaseLogger import BaseLogger

class Tests:
    def __init__(self, test_file_path=None):
        if not test_file_path:
            raise TypeError('Required argument \'test_file_path\' missing')
        self.testConfigFile = test_file_path
        with open(self.testConfigFile, 'r') as ymlfile:
            try:
                data = yaml.safe_load(ymlfile)
                self._testCount = len(data.get('tests'))
                self._testList = data.get('tests')
                BaseLogger.info('Found ' + str(self._testCount) + ' tests ...')
            except yaml.YAMLError as error:
                print(error)

    def getTestCount(self):
        # Return Test Count
        return self._testCount

    def getTestName(self, test_index):
        # Return Test Name With The Given test_index
        if test_index > self._testCount:
            return False
        key = list(self._testList.keys())[test_index]
        return self._testList.get(key).get('name')

    def getTestDescription(self, test_index):
        # Return Test Description With The Given test_index
        if test_index > self._testCount:
            return False
        key = list(self._testList.keys())[test_index]
        return self._testList.get(key).get('description')
    
    def getTestFileName(self, test_index):
        # Return Test File Path With The Given test_index
        if test_index > self._testCount:
            return False
        key = list(self._testList.keys())[test_index]
        return self._testList.get(key).get('file')

    def getTestAbsoluteFolderPath(self, test_index):
        # Return Absolute Folder Path With The Given test_index
        return '/home/pi/xenovia/tests/' + self.getTestFileName(test_index)[:-3]
        
    def getTestIndexFromName(self, test_name):
        # Return Test Index From The Test Name
        if not test_name:
            raise TypeError('Required argument missing')
        index = 0
        for tests in self._testList.values():
            if test_name == tests.get('name'):
                return index
            index += 1
        return -1

    def getTestReference(self, test_index):
        # Return Test Class Reference With The Given test_index
        if test_index > self._testCount:
            return False
        # Load Class Module
        module = importlib.import_module('tests' + \
                                            '.' + \
                                            (self.getTestFileName(test_index))[:-3] + \
                                            '.' + \
                                            (self.getTestFileName(test_index))[:-3])
        
        attr = getattr(module,(self.getTestFileName(test_index))[:-3])
        return attr