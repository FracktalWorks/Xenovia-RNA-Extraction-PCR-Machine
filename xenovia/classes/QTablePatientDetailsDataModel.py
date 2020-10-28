#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: June 2020
 *
 * CSV Data Model Class For QTable
 * Reference
 *      https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor

class QTablePatientDetailsDataModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)
    
    def load_data(self, data):
        self.input_tube = data[0].values
        self.input_name = data[1].values
        self.input_sample_id = data[2].values
        self.input_gender = data[3].values
        self.input_age = data[4].values
        self.input_remarks = data[5].values

        self.column_count = 6
        self.row_count = len(self.input_tube)
    
    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.column_count
    
    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            return ('Tube', 'Name', 'Sample Id', 'Gender', 'Age', 'Remarks')[section]
        else:
            return "{}".format(section)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return self.input_tube[row]
            elif column == 1:
                return self.input_name[row]
            elif column == 2:
                return str(self.input_sample_id[row])
            elif column == 3:
                return self.input_gender[row]
            elif column == 4:
                return str(self.input_age[row])
            elif column == 5:
                return self.input_remarks[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None