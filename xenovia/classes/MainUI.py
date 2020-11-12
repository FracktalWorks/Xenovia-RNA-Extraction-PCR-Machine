#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Main UI Class
 * All Slots And Events Defined Within
 *
 * Licence: PROPRIETARY
*************************************************************************
'''

import os
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

from ui import xenovia_ui
from classes.TipHolderTray import TipHolderTray
from classes.WellTray import WellTray
from classes.TipTrash import TipTrash
from classes.Pipette import Pipette
from classes.Magnet import Magnet
from classes.PCRTray import PCRTray
from classes.QTablePatientDetailsDataModel import QTablePatientDetailsDataModel
from helpers.BaseLogger import BaseLogger
from helpers.CSV import *

class OkCancelDialog():
    # OK / Cancel Dialog Box

    # Defines
    DEFINE_MESSAGE_BOX_QUESTION = QMessageBox.Question
    DEFINE_MESSAGE_BOX_INFORMATION = QMessageBox.Information
    DEFINE_MESSAGE_BOX_WARNING = QMessageBox.Warning
    DEFINE_MESSAGE_BOX_CRITICAL = QMessageBox.Critical

    msg_box = None

    def __init__(self, title, message, icon, fn_btn_press):
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(icon)
        self.msg_box.setWindowTitle(title)
        self.msg_box.setText(message)
        self.msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg_box.buttonClicked.connect(fn_btn_press)

    def show(self):
        self.msg_box.exec_()

class MainUI(QMainWindow, xenovia_ui.Ui_MainWindow):
    '''
    Main GUI Workhorse, all slots and events defined within
    The main implementation class that inherits methods, variables etc
    '''

    # Defines
    DEFINE_SCREEN_MAIN = 0
    DEFINE_SCREEN_TEST_CHOOSE = 1
    DEFINE_SCREEN_PATIENT_DETAILS = 2
    DEFINE_SCREEN_ADD_VTM_SAMPLES = 3
    DEFINE_SCREEN_PLACE_TIP_WELL = 4
    DEFINE_SCREEN_TEST_RUNNING = 5
    DEFINE_SCREEN_TEST_RESULT = 6
    DEFINE_SCREEN_ABOUT = 7
    DEFINE_SCREEN_SETTINGS = 9
    DEFINE_SCREEN_HELP = 11

    DEFINE_TESTS_GRID_MAX_X = 4

    DEFINE_TESTS_GRID_BUTTON_SIZE_X = 150
    DEFINE_TESTS_GRID_BUTTON_SIZE_Y = 75
    
    path_ui_file = '/home/pi/xenovia/ui/xenovia_ui.ui'

    # Variables
    handle_printer = None
    handle_tests = None
    handle_current_test = None
    handle_tip_tray = None
    handle_well_tray = None
    handle_pcr_tray = None
    handle_trash_tray = None
    handle_pipette = None
    handle_magnet = None

    tests_list = []
    current_test_index = None
    current_test_pd_file_path = None
    test_list_button_group = None

    test_imagebox_signal = pyqtSignal(str)
    test_textbox_signal = pyqtSignal(str)
    test_progressbar_signal = pyqtSignal(int)
    test_abort_signal = pyqtSignal()
    test_finish_signal = pyqtSignal()

    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi(self.path_ui_file, self)

        # Setup UI Signals / Slots
        self.setupButtons()
        self.setupSignalSlots()

        # Setup Main Window
        self.showMainScreen()
        
        self.show()
        self.showFullScreen()
        BaseLogger.info('gui loaded')

    def setHandlePrinter(self, printer=None):
        # Set Printer Handle
        if not printer:
            raise TypeError('Required argument missing')
        self.handle_printer = printer
        self.handle_tip_tray = TipHolderTray(self.handle_printer)
        self.handle_well_tray = WellTray(self.handle_printer)
        self.handle_pcr_tray =  PCRTray(self.handle_printer)
        self.handle_trash_tray = TipTrash(self.handle_printer)
        self.handle_pipette = Pipette(self.handle_printer)
        self.handle_magnet = Magnet(self.handle_printer)
        self.handle_printer.moveServo(0,0)

    def setHandleTests(self, tests=None):
        # Set Tests Handle
        if not tests:
            raise TypeError('Required argument missing')
        self.handle_tests = tests

    def setupButtons(self):
        # Setup Buttons
        # Define All Button Click Actions
        # Main Screen
        self.newRunButton.clicked.connect(lambda: self.showTestsScreen())
        self.settingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_SETTINGS))
        self.aboutButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_ABOUT))
        self.helpButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_HELP))

        # Tests Screen
        self.cpBackButton.clicked.connect(lambda: self.showMainScreen())
        # self.cpNextButton.clicked.connect(lambda: self.showPatientDetailsScreen())
        self.cpNextButton.clicked.connect(lambda: self.showVTMScreen()) # skips patient details screen for the moment

        # Patient Details Screen
        self.pdBackButton.clicked.connect(lambda: self.showTestsScreen())
        self.pdLoadDataButton.clicked.connect(lambda: self.showFileSelector())
        self.pdNextButton.clicked.connect(lambda: self.showVTMScreen())       

        # VTM Screen
        self.vtmBackButton.clicked.connect(lambda: self.showPatientDetailsScreen())
        self.vtmNextButton.clicked.connect(lambda: self.showTipWellScreen())

        # TIP WELL Screen
        self.insertBackButton.clicked.connect(lambda: self.showVTMScreen())
        self.insertMainMenuBackButton.clicked.connect(lambda: self.showMainScreen())
        self.insertOkButton.clicked.connect(lambda: self.startTest())

        # Running Screen
        self.nrStopButton.clicked.connect(lambda: self.abortTest())
        
        # Test Result Screen
        self.exitButton.clicked.connect(lambda: self.showMainScreen())

        # Settings Screen
        self.settingsHomeButton.clicked.connect(lambda: self.handle_printer.home())
        self.settingsHomeYButton.clicked.connect(lambda: self.handle_printer.homeY())
        self.settingsHomeZButton.clicked.connect(lambda: self.handle_printer.homeZ())
        self.settingsYPlus1Button.clicked.connect(lambda: self.handle_printer.moveYRelative(1))
        self.settingsYPlus10Button.clicked.connect(lambda: self.handle_printer.moveYRelative(10))
        self.settingsYPlus100Button.clicked.connect(lambda: self.handle_printer.moveYRelative(100))
        self.settingsYMinus1Button.clicked.connect(lambda: self.handle_printer.moveYRelative(-1))
        self.settingsYMinus10Button.clicked.connect(lambda: self.handle_printer.moveYRelative(-10))
        self.settingsYMinus100Button.clicked.connect(lambda: self.handle_printer.moveYRelative(-100))
        self.settingsZPlus1Button.clicked.connect(lambda: self.handle_printer.moveZRelative(1))
        self.settingsZPlus10Button.clicked.connect(lambda: self.handle_printer.moveZRelative(10))
        self.settingsZPlus100Button.clicked.connect(lambda: self.handle_printer.moveZRelative(100))
        self.settingsZMinus1Button.clicked.connect(lambda: self.handle_printer.moveZRelative(-1))
        self.settingsZMinus10Button.clicked.connect(lambda: self.handle_printer.moveZRelative(-10))
        self.settingsZMinus100Button.clicked.connect(lambda: self.handle_printer.moveZRelative(-100))
        self.settingsTipTrashButton.clicked.connect(lambda: self.handle_trash_tray.trashTips())
        self.settingsLeftMagnetOnButton.clicked.connect(lambda: self.handle_magnet.engage(Magnet.MAGNET_0))
        self.settingsLeftMagnetOffButton.clicked.connect(lambda: self.handle_magnet.disengage(Magnet.MAGNET_0))
        self.settingsRightMagnetOnButton.clicked.connect(lambda: self.handle_magnet.engage(Magnet.MAGNET_1))
        self.settingsRightMagnetOffButton.clicked.connect(lambda: self.handle_magnet.disengage(Magnet.MAGNET_1))
        self.settingsPAsperateButton.clicked.connect(lambda: self.handle_pipette.aspirate(Pipette.PIPETTE_LEVEL_UL_200))
        self.settingsPDispenseButton.clicked.connect(lambda: self.handle_pipette.dispense())
        self.settingsBackButton.clicked.connect(lambda: self.showMainScreen())    

        # Help Screen
        self.helpBackButton.clicked.connect(lambda: self.showMainScreen())

        #About Screen
        self.mainMenuBackButton.clicked.connect(lambda: self.showMainScreen())

    def setupSignalSlots(self):
        # Setup Custom Signals & Slots
        self.test_progressbar_signal.connect(lambda x: self.nrProgressBar.setValue(x))
        self.test_imagebox_signal.connect(lambda x: self.nrImageDisplay.setStyleSheet( \
            'background-image: url("' + self.handle_tests.getTestAbsoluteFolderPath(self.current_test_index) + '/resources/' + x + '");'))
        self.test_textbox_signal.connect(lambda x: self.nrStatusLabel.setText(x))
        self.test_abort_signal.connect(lambda: self.testAborted())
        self.test_finish_signal.connect(lambda: self.testFinished())

    def showMainScreen(self):
        # Show Main Screen
        self.current_test_index = None
        self.current_test_pd_file_path = None
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_MAIN)

    def showTestsScreen(self):
        # Show Tests Screen
        # Populate Available Tests
        layout = self.chooseProgramGridLayout
        self.cpNextButton.setEnabled(False)
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_TEST_CHOOSE)
        self.test_list_button_group = QButtonGroup()
        self.test_list_button_group.setExclusive(True)
        x = 0
        y = 0
        button_size = QSize(self. DEFINE_TESTS_GRID_BUTTON_SIZE_X, \
            self.DEFINE_TESTS_GRID_BUTTON_SIZE_Y)
        for i in range(self.handle_tests.getTestCount()):
            button = QPushButton()
            button.setText(self.handle_tests.getTestName(i))
            button.setCheckable(True)
            button.setFixedSize(button_size)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Gotham Medium"))
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            button.setFont(font)
            button.setStyleSheet(_fromUtf8("QPushButton {\n"
                                              "     border: 1px solid rgb(87, 87, 87);\n"
                                              "    border-right: none;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n" 
                                              "color : black;\n"
                                              "    \n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                              "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:flat {\n"
                                              "    border: none; /* no border for a flat push button */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:default {\n"
                                              "    border-color: navy; /* make the default button prominent */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:focus {\n"
                                              "    outline: none;\n"
                                              "}"))
            self.test_list_button_group.addButton(button)
            if x >= self.DEFINE_TESTS_GRID_MAX_X:
                x = 0
                y = y + 1
            layout.addWidget(button, y, x)
            x += 1
            self.tests_list.append(button)
        self.test_list_button_group.buttonClicked[int].connect(self.testsListbuttonGroupOnClick)

    def testsListbuttonGroupOnClick(self, index):
        # Tests List Button Group Callback
        test_text = self.test_list_button_group.button(index).text()
        self.cpNextButton.setEnabled(True)
        BaseLogger.info('selected test : ' + test_text)
        test_index = self.handle_tests.getTestIndexFromName(test_text)
        self.current_test_index = test_index
        BaseLogger.info('test index : ' + str(test_index))
        BaseLogger.info('test description : ' + self.handle_tests.getTestDescription(test_index))
        BaseLogger.info('test filename : ' + self.handle_tests.getTestFileName(test_index))

    def showPatientDetailsScreen(self):
        # Show Patient Details Screen
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_PATIENT_DETAILS)
        self.pdSelectedProgramLabel.setText(self.handle_tests.getTestName(self.current_test_index))
        if not self.current_test_pd_file_path:
            self.pdNextButton.setEnabled(False)
            self.pdSkipButton.setEnabled(False)
            self.pdTableView.setModel(QStandardItemModel())
        else:
            self.pdNextButton.setEnabled(True)
            # Load CSV Data
            table_data = CSVRead(self.current_test_pd_file_path)
            self.pdTableView.setModel(QTablePatientDetailsDataModel(table_data))

    def showFileSelector(self):
        # Show QT File Selector
        selector = QFileDialog(self, 'Select CSV File', '/home/pi','CSV files(*.csv)')
        filenames = []
        if selector.exec_():
            filenames = selector.selectedFiles()
        if len(filenames) != 0:
            # CSV File Selected
            BaseLogger.info('PD File : ' + filenames[0])
            self.pdNextButton.setEnabled(True)
            # Load CSV Data
            table_data = CSVRead(filenames[0])
            self.pdTableView.setModel(QTablePatientDetailsDataModel(table_data))
            self.current_test_pd_file_path = filenames[0]

    def showVTMScreen(self):
        # Show VTM Screen
        self.handle_printer.moveServo(0, 0)
        self.vtmSelectedProgramLabel.setText(self.handle_tests.getTestName(self.current_test_index))
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_ADD_VTM_SAMPLES)
    
    def showTipWellScreen(self):
        # Show Tip Well Screen
        self.insertProgramSelectedLabel.setText(self.handle_tests.getTestName(self.current_test_index))
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_PLACE_TIP_WELL)
    
    def startTest(self):
        # Start Selected Test
        self.nrProgramSelectedLabel.setText(self.handle_tests.getTestName(self.current_test_index))
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_TEST_RUNNING)
        test_reference = self.handle_tests.getTestReference(self.current_test_index)
        self.handle_current_test = test_reference(self.handle_printer,  \
                                    self.handle_tip_tray, \
                                    self.handle_well_tray, \
                                    self.handle_pcr_tray,\
                                    self.handle_trash_tray, \
                                    self.handle_pipette, \
                                    self.handle_magnet, \
                                    self.test_imagebox_signal, \
                                    self.test_textbox_signal, \
                                    self.test_progressbar_signal,
                                    self.test_abort_signal,
                                    self.test_finish_signal)
        #self.nrImageDisplay.setFrameStyle(6)                            
        # Home Printer Before Starting Test
        self.handle_printer.home()
        # Start Test
        self.handle_current_test.start()

    def abortTest(self):
        # Abort Currently Running Test
        warning = OkCancelDialog('Confirm', \
                    'Are you sure you want to abort\n the test ?', \
                    OkCancelDialog.DEFINE_MESSAGE_BOX_WARNING, \
                    self.abortTestDialogButtonPress)
        warning.show()

    def abortTestDialogButtonPress(self, button):
        # Abort Test Confirmation Dialog Button Press Cb
        if button.text() == 'OK':
            self.handle_current_test.abortTest()

    def testAborted(self):
        # Test Aborted
        self.showMainScreen()
        pass
    
    def testFinished(self):
        # Test Finished
        self.handle_printer.home()
        self.showTestResultScreen()
        pass

    def showTestResultScreen(self):
        # Show Test Result Screen
        self.nrProgramSelectedLabel.setText(self.handle_tests.getTestName(self.current_test_index))
        self.stackedWidget.setCurrentIndex(self.DEFINE_SCREEN_TEST_RESULT)
