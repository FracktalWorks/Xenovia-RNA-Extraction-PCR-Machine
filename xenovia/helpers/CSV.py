#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * CSV Reading / Writing Helper Routines
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import csv
import pandas as pd

def CSVRead(file_path=None):
    # Read CSV File Specified By filepath And Return Data
    # As Set Of Columns
    if not file_path:
        raise TypeError('file_path error')
    dataset = pd.read_csv(file_path)
    return dataset['tube'], dataset['name'], dataset['sample_id'], dataset['gender'], dataset['age'], dataset['remarks']

def CSVWrite(file_path=None, data=None, field_names=None):
    # Save Dictionary List Data In CSV File Specified By file_path
    # Field Names In List field_names
    if not file_path or not data or not field_names:
        raise TypeError("file_path, data error or field_names error")
    f = open(file_path, mode='w')
    with f as output_file:
        writer = csv.DictWriter(output_file, fieldname=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    f.close()
