#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Licence: PROPRIETARY
************************
'''

import logging

# Set Up Base Logger

grey = "\x1b[38;21m"
yellow = "\x1b[33;21m"
red = "\x1b[31;21m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"

format = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%d-%m-%Y %H:%M:%S')

BaseLogger = logging.getLogger(__name__)

file_handler = logging.FileHandler('/home/pi/xenovia/log/xenovia.log')
stream_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)

file_handler.setFormatter(format)
stream_handler.setFormatter(format)

BaseLogger.addHandler(file_handler)
BaseLogger.addHandler(stream_handler)

BaseLogger.setLevel(logging.DEBUG)
