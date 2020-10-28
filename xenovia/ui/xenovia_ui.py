# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xenovia_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(0, 0, 0);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainMenu = QtWidgets.QWidget()
        self.mainMenu.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(0, 0, 0);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.mainMenu.setObjectName("mainMenu")
        self.newRunButton = QtWidgets.QPushButton(self.mainMenu)
        self.newRunButton.setGeometry(QtCore.QRect(-1, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newRunButton.setFont(font)
        self.newRunButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.newRunButton.setObjectName("newRunButton")
        self.patientReportButton = QtWidgets.QPushButton(self.mainMenu)
        self.patientReportButton.setGeometry(QtCore.QRect(199, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.patientReportButton.setFont(font)
        self.patientReportButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.patientReportButton.setObjectName("patientReportButton")
        self.settingsButton = QtWidgets.QPushButton(self.mainMenu)
        self.settingsButton.setGeometry(QtCore.QRect(399, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingsButton.setFont(font)
        self.settingsButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsButton.setObjectName("settingsButton")
        self.helpButton = QtWidgets.QPushButton(self.mainMenu)
        self.helpButton.setGeometry(QtCore.QRect(599, 0, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.helpButton.setFont(font)
        self.helpButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.helpButton.setObjectName("helpButton")
        self.aboutButton = QtWidgets.QPushButton(self.mainMenu)
        self.aboutButton.setGeometry(QtCore.QRect(599, 360, 201, 120))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.aboutButton.setObjectName("aboutButton")
        self.mainMenuLabel = QtWidgets.QLabel(self.mainMenu)
        self.mainMenuLabel.setGeometry(QtCore.QRect(10, 10, 290, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.mainMenuLabel.setFont(font)
        self.mainMenuLabel.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.mainMenuLabel.setObjectName("mainMenuLabel")
        self.label = QtWidgets.QLabel(self.mainMenu)
        self.label.setGeometry(QtCore.QRect(630, 200, 141, 61))
        self.label.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.mainMenu)
        self.chooseProgram = QtWidgets.QWidget()
        self.chooseProgram.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.chooseProgram.setObjectName("chooseProgram")
        self.cpLabel = QtWidgets.QLabel(self.chooseProgram)
        self.cpLabel.setGeometry(QtCore.QRect(300, 0, 241, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cpLabel.setFont(font)
        self.cpLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.cpLabel.setObjectName("cpLabel")
        self.cpBackButton = QtWidgets.QPushButton(self.chooseProgram)
        self.cpBackButton.setGeometry(QtCore.QRect(0, 360, 401, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cpBackButton.setFont(font)
        self.cpBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.cpBackButton.setObjectName("cpBackButton")
        self.cpNextButton = QtWidgets.QPushButton(self.chooseProgram)
        self.cpNextButton.setGeometry(QtCore.QRect(400, 360, 401, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cpNextButton.setFont(font)
        self.cpNextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.cpNextButton.setObjectName("cpNextButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.chooseProgram)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 30, 781, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chooseProgramGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chooseProgramGridLayout.setContentsMargins(0, 0, 0, 0)
        self.chooseProgramGridLayout.setVerticalSpacing(8)
        self.chooseProgramGridLayout.setObjectName("chooseProgramGridLayout")
        self.stackedWidget.addWidget(self.chooseProgram)
        self.patientDetails = QtWidgets.QWidget()
        self.patientDetails.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.patientDetails.setObjectName("patientDetails")
        self.pdLabel = QtWidgets.QLabel(self.patientDetails)
        self.pdLabel.setGeometry(QtCore.QRect(330, 0, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pdLabel.setFont(font)
        self.pdLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.pdLabel.setObjectName("pdLabel")
        self.pdBackButton = QtWidgets.QPushButton(self.patientDetails)
        self.pdBackButton.setGeometry(QtCore.QRect(-1, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pdBackButton.setFont(font)
        self.pdBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.pdBackButton.setObjectName("pdBackButton")
        self.pdSkipButton = QtWidgets.QPushButton(self.patientDetails)
        self.pdSkipButton.setGeometry(QtCore.QRect(399, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pdSkipButton.setFont(font)
        self.pdSkipButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.pdSkipButton.setObjectName("pdSkipButton")
        self.pdNextButton = QtWidgets.QPushButton(self.patientDetails)
        self.pdNextButton.setGeometry(QtCore.QRect(599, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pdNextButton.setFont(font)
        self.pdNextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.pdNextButton.setObjectName("pdNextButton")
        self.pdTableView = QtWidgets.QTableView(self.patientDetails)
        self.pdTableView.setGeometry(QtCore.QRect(10, 29, 780, 311))
        self.pdTableView.setObjectName("pdTableView")
        self.pdLoadDataButton = QtWidgets.QPushButton(self.patientDetails)
        self.pdLoadDataButton.setGeometry(QtCore.QRect(199, 360, 201, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pdLoadDataButton.setFont(font)
        self.pdLoadDataButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.pdLoadDataButton.setObjectName("pdLoadDataButton")
        self.pdSelectedProgramLabel = QtWidgets.QLabel(self.patientDetails)
        self.pdSelectedProgramLabel.setGeometry(QtCore.QRect(0, 0, 151, 21))
        self.pdSelectedProgramLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.pdSelectedProgramLabel.setObjectName("pdSelectedProgramLabel")
        self.stackedWidget.addWidget(self.patientDetails)
        self.addVTMSamples = QtWidgets.QWidget()
        self.addVTMSamples.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.addVTMSamples.setObjectName("addVTMSamples")
        self.vtmLabel = QtWidgets.QLabel(self.addVTMSamples)
        self.vtmLabel.setGeometry(QtCore.QRect(240, 0, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtmLabel.setFont(font)
        self.vtmLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.vtmLabel.setObjectName("vtmLabel")
        self.vtmBackButton = QtWidgets.QPushButton(self.addVTMSamples)
        self.vtmBackButton.setGeometry(QtCore.QRect(-1, 360, 411, 120))
        self.vtmBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.vtmBackButton.setObjectName("vtmBackButton")
        self.vtmNextButton = QtWidgets.QPushButton(self.addVTMSamples)
        self.vtmNextButton.setGeometry(QtCore.QRect(410, 360, 391, 120))
        self.vtmNextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.vtmNextButton.setObjectName("vtmNextButton")
        self.vtmSelectedProgramLabel = QtWidgets.QLabel(self.addVTMSamples)
        self.vtmSelectedProgramLabel.setGeometry(QtCore.QRect(0, 0, 171, 21))
        self.vtmSelectedProgramLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.vtmSelectedProgramLabel.setObjectName("vtmSelectedProgramLabel")
        self.vtmImage = QtWidgets.QLabel(self.addVTMSamples)
        self.vtmImage.setGeometry(QtCore.QRect(180, 60, 460, 280))
        self.vtmImage.setText("")
        self.vtmImage.setTextFormat(QtCore.Qt.PlainText)
        self.vtmImage.setPixmap(QtGui.QPixmap("Resources/vtm.png"))
        self.vtmImage.setObjectName("vtmImage")
        self.stackedWidget.addWidget(self.addVTMSamples)
        self.placeTipWell = QtWidgets.QWidget()
        self.placeTipWell.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.placeTipWell.setObjectName("placeTipWell")
        self.insertLabel1 = QtWidgets.QLabel(self.placeTipWell)
        self.insertLabel1.setGeometry(QtCore.QRect(170, 0, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.insertLabel1.setFont(font)
        self.insertLabel1.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.insertLabel1.setObjectName("insertLabel1")
        self.insertLabel2 = QtWidgets.QLabel(self.placeTipWell)
        self.insertLabel2.setGeometry(QtCore.QRect(350, 90, 81, 20))
        self.insertLabel2.setText("")
        self.insertLabel2.setObjectName("insertLabel2")
        self.insertBackButton = QtWidgets.QPushButton(self.placeTipWell)
        self.insertBackButton.setGeometry(QtCore.QRect(-1, 360, 271, 120))
        self.insertBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.insertBackButton.setObjectName("insertBackButton")
        self.insertMainMenuBackButton = QtWidgets.QPushButton(self.placeTipWell)
        self.insertMainMenuBackButton.setGeometry(QtCore.QRect(539, 360, 261, 120))
        self.insertMainMenuBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.insertMainMenuBackButton.setObjectName("insertMainMenuBackButton")
        self.insertOkButton = QtWidgets.QPushButton(self.placeTipWell)
        self.insertOkButton.setGeometry(QtCore.QRect(269, 360, 271, 120))
        self.insertOkButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.insertOkButton.setObjectName("insertOkButton")
        self.insertImage = QtWidgets.QLabel(self.placeTipWell)
        self.insertImage.setGeometry(QtCore.QRect(190, 50, 420, 280))
        self.insertImage.setText("")
        self.insertImage.setPixmap(QtGui.QPixmap("Resources/insert.png"))
        self.insertImage.setObjectName("insertImage")
        self.insertProgramSelectedLabel = QtWidgets.QLabel(self.placeTipWell)
        self.insertProgramSelectedLabel.setGeometry(QtCore.QRect(0, 0, 121, 21))
        self.insertProgramSelectedLabel.setStyleSheet("QLabel{\n"
"color : white;}")
        self.insertProgramSelectedLabel.setObjectName("insertProgramSelectedLabel")
        self.stackedWidget.addWidget(self.placeTipWell)
        self.nuampRunning = QtWidgets.QWidget()
        self.nuampRunning.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.nuampRunning.setObjectName("nuampRunning")
        self.nrPauseButton = QtWidgets.QPushButton(self.nuampRunning)
        self.nrPauseButton.setGeometry(QtCore.QRect(-1, 360, 201, 120))
        self.nrPauseButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.nrPauseButton.setObjectName("nrPauseButton")
        self.nrStopButton = QtWidgets.QPushButton(self.nuampRunning)
        self.nrStopButton.setGeometry(QtCore.QRect(600, 360, 201, 120))
        self.nrStopButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.nrStopButton.setObjectName("nrStopButton")
        self.nrStatusLabel = QtWidgets.QLabel(self.nuampRunning)
        self.nrStatusLabel.setGeometry(QtCore.QRect(209, 360, 381, 120))
        self.nrStatusLabel.setObjectName("nrStatusLabel")
        self.nrLabel = QtWidgets.QLabel(self.nuampRunning)
        self.nrLabel.setGeometry(QtCore.QRect(330, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nrLabel.setFont(font)
        self.nrLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.nrLabel.setObjectName("nrLabel")
        self.nrProgressBar = QtWidgets.QProgressBar(self.nuampRunning)
        self.nrProgressBar.setGeometry(QtCore.QRect(10, 320, 781, 20))
        self.nrProgressBar.setStyleSheet("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}")
        self.nrProgressBar.setProperty("value", 24)
        self.nrProgressBar.setObjectName("nrProgressBar")
        self.nrImageDisplay = QtWidgets.QLabel(self.nuampRunning)
        self.nrImageDisplay.setGeometry(QtCore.QRect(10, 40, 780, 261))
        self.nrImageDisplay.setAutoFillBackground(False)
        self.nrImageDisplay.setStyleSheet("")
        self.nrImageDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nrImageDisplay.setMidLineWidth(-4)
        self.nrImageDisplay.setObjectName("nrImageDisplay")
        self.nrProgramSelectedLabel = QtWidgets.QLabel(self.nuampRunning)
        self.nrProgramSelectedLabel.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.nrProgramSelectedLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.nrProgramSelectedLabel.setObjectName("nrProgramSelectedLabel")
        self.stackedWidget.addWidget(self.nuampRunning)
        self.nuampResult = QtWidgets.QWidget()
        self.nuampResult.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.nuampResult.setObjectName("nuampResult")
        self.nrLabel_2 = QtWidgets.QLabel(self.nuampResult)
        self.nrLabel_2.setGeometry(QtCore.QRect(270, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nrLabel_2.setFont(font)
        self.nrLabel_2.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.nrLabel_2.setObjectName("nrLabel_2")
        self.exitButton = QtWidgets.QPushButton(self.nuampResult)
        self.exitButton.setGeometry(QtCore.QRect(-1, 360, 271, 120))
        self.exitButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.exitButton.setObjectName("exitButton")
        self.generatePDFButton = QtWidgets.QPushButton(self.nuampResult)
        self.generatePDFButton.setGeometry(QtCore.QRect(539, 360, 261, 120))
        self.generatePDFButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.generatePDFButton.setObjectName("generatePDFButton")
        self.nrTableView = QtWidgets.QTableView(self.nuampResult)
        self.nrTableView.setGeometry(QtCore.QRect(10, 39, 780, 311))
        self.nrTableView.setObjectName("nrTableView")
        self.nrSaveDataButton = QtWidgets.QPushButton(self.nuampResult)
        self.nrSaveDataButton.setGeometry(QtCore.QRect(269, 360, 271, 120))
        self.nrSaveDataButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.nrSaveDataButton.setObjectName("nrSaveDataButton")
        self.nrProgramSelectedLabel_2 = QtWidgets.QLabel(self.nuampResult)
        self.nrProgramSelectedLabel_2.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.nrProgramSelectedLabel_2.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.nrProgramSelectedLabel_2.setObjectName("nrProgramSelectedLabel_2")
        self.stackedWidget.addWidget(self.nuampResult)
        self.about = QtWidgets.QWidget()
        self.about.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.about.setObjectName("about")
        self.contactInfoTextBrowser = QtWidgets.QTextBrowser(self.about)
        self.contactInfoTextBrowser.setGeometry(QtCore.QRect(10, 11, 781, 331))
        self.contactInfoTextBrowser.setStyleSheet("")
        self.contactInfoTextBrowser.setObjectName("contactInfoTextBrowser")
        self.mainMenuBackButton = QtWidgets.QPushButton(self.about)
        self.mainMenuBackButton.setGeometry(QtCore.QRect(0, 360, 801, 120))
        self.mainMenuBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.mainMenuBackButton.setObjectName("mainMenuBackButton")
        self.stackedWidget.addWidget(self.about)
        self.mainSettings = QtWidgets.QWidget()
        self.mainSettings.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.mainSettings.setObjectName("mainSettings")
        self.stackedWidget.addWidget(self.mainSettings)
        self.settings = QtWidgets.QWidget()
        self.settings.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.settings.setObjectName("settings")
        self.settingsHomeButton = QtWidgets.QPushButton(self.settings)
        self.settingsHomeButton.setGeometry(QtCore.QRect(10, 80, 120, 80))
        self.settingsHomeButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsHomeButton.setObjectName("settingsHomeButton")
        self.settingsHomeYButton = QtWidgets.QPushButton(self.settings)
        self.settingsHomeYButton.setGeometry(QtCore.QRect(10, 180, 120, 80))
        self.settingsHomeYButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsHomeYButton.setObjectName("settingsHomeYButton")
        self.settingsHomeZButton = QtWidgets.QPushButton(self.settings)
        self.settingsHomeZButton.setGeometry(QtCore.QRect(10, 280, 120, 80))
        self.settingsHomeZButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsHomeZButton.setObjectName("settingsHomeZButton")
        self.settingsYPlus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsYPlus100Button.setGeometry(QtCore.QRect(180, 90, 80, 60))
        self.settingsYPlus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYPlus100Button.setObjectName("settingsYPlus100Button")
        self.settingsYPlus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsYPlus10Button.setGeometry(QtCore.QRect(270, 90, 80, 60))
        self.settingsYPlus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYPlus10Button.setObjectName("settingsYPlus10Button")
        self.settingsYPlus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsYPlus1Button.setGeometry(QtCore.QRect(360, 90, 80, 60))
        self.settingsYPlus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYPlus1Button.setObjectName("settingsYPlus1Button")
        self.settingsLeftMagnetOnButton = QtWidgets.QPushButton(self.settings)
        self.settingsLeftMagnetOnButton.setGeometry(QtCore.QRect(160, 390, 101, 80))
        self.settingsLeftMagnetOnButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsLeftMagnetOnButton.setObjectName("settingsLeftMagnetOnButton")
        self.settingsBackButton = QtWidgets.QPushButton(self.settings)
        self.settingsBackButton.setGeometry(QtCore.QRect(10, 390, 120, 80))
        self.settingsBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsBackButton.setObjectName("settingsBackButton")
        self.settingsYMinus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsYMinus1Button.setGeometry(QtCore.QRect(530, 90, 80, 60))
        self.settingsYMinus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYMinus1Button.setObjectName("settingsYMinus1Button")
        self.settingsYMinus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsYMinus10Button.setGeometry(QtCore.QRect(620, 90, 80, 60))
        self.settingsYMinus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYMinus10Button.setObjectName("settingsYMinus10Button")
        self.settingsYMinus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsYMinus100Button.setGeometry(QtCore.QRect(710, 90, 80, 60))
        self.settingsYMinus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsYMinus100Button.setObjectName("settingsYMinus100Button")
        self.settingsYLabel = QtWidgets.QLabel(self.settings)
        self.settingsYLabel.setGeometry(QtCore.QRect(470, 90, 40, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.settingsYLabel.setFont(font)
        self.settingsYLabel.setObjectName("settingsYLabel")
        self.settingsZMinus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsZMinus10Button.setGeometry(QtCore.QRect(620, 190, 80, 60))
        self.settingsZMinus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZMinus10Button.setObjectName("settingsZMinus10Button")
        self.settingsZPlus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsZPlus100Button.setGeometry(QtCore.QRect(180, 190, 80, 60))
        self.settingsZPlus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZPlus100Button.setObjectName("settingsZPlus100Button")
        self.settingsZPlus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsZPlus10Button.setGeometry(QtCore.QRect(270, 190, 80, 60))
        self.settingsZPlus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZPlus10Button.setObjectName("settingsZPlus10Button")
        self.settingsZMinus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsZMinus100Button.setGeometry(QtCore.QRect(710, 190, 80, 60))
        self.settingsZMinus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZMinus100Button.setObjectName("settingsZMinus100Button")
        self.settingsZLabel = QtWidgets.QLabel(self.settings)
        self.settingsZLabel.setGeometry(QtCore.QRect(470, 190, 40, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.settingsZLabel.setFont(font)
        self.settingsZLabel.setObjectName("settingsZLabel")
        self.settingsZPlus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsZPlus1Button.setGeometry(QtCore.QRect(360, 190, 80, 60))
        self.settingsZPlus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZPlus1Button.setObjectName("settingsZPlus1Button")
        self.settingsZMinus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsZMinus1Button.setGeometry(QtCore.QRect(530, 190, 80, 60))
        self.settingsZMinus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsZMinus1Button.setObjectName("settingsZMinus1Button")
        self.settingsLeftMagnetOffButton = QtWidgets.QPushButton(self.settings)
        self.settingsLeftMagnetOffButton.setGeometry(QtCore.QRect(270, 390, 101, 80))
        self.settingsLeftMagnetOffButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsLeftMagnetOffButton.setObjectName("settingsLeftMagnetOffButton")
        self.settingsPAsperateButton = QtWidgets.QPushButton(self.settings)
        self.settingsPAsperateButton.setGeometry(QtCore.QRect(600, 390, 91, 80))
        self.settingsPAsperateButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPAsperateButton.setObjectName("settingsPAsperateButton")
        self.settingsPDispenseButton = QtWidgets.QPushButton(self.settings)
        self.settingsPDispenseButton.setGeometry(QtCore.QRect(699, 390, 91, 80))
        self.settingsPDispenseButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPDispenseButton.setObjectName("settingsPDispenseButton")
        self.settingsPMinus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsPMinus100Button.setGeometry(QtCore.QRect(710, 290, 80, 60))
        self.settingsPMinus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPMinus100Button.setObjectName("settingsPMinus100Button")
        self.settingsPLabel = QtWidgets.QLabel(self.settings)
        self.settingsPLabel.setGeometry(QtCore.QRect(470, 290, 40, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.settingsPLabel.setFont(font)
        self.settingsPLabel.setObjectName("settingsPLabel")
        self.settingsPMinus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsPMinus10Button.setGeometry(QtCore.QRect(620, 290, 80, 60))
        self.settingsPMinus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPMinus10Button.setObjectName("settingsPMinus10Button")
        self.settingsPPlus10Button = QtWidgets.QPushButton(self.settings)
        self.settingsPPlus10Button.setGeometry(QtCore.QRect(270, 290, 80, 60))
        self.settingsPPlus10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPPlus10Button.setObjectName("settingsPPlus10Button")
        self.settingsPPlus100Button = QtWidgets.QPushButton(self.settings)
        self.settingsPPlus100Button.setGeometry(QtCore.QRect(180, 290, 80, 60))
        self.settingsPPlus100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPPlus100Button.setObjectName("settingsPPlus100Button")
        self.settingsPPlus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsPPlus1Button.setGeometry(QtCore.QRect(360, 290, 80, 60))
        self.settingsPPlus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPPlus1Button.setObjectName("settingsPPlus1Button")
        self.settingsPMinus1Button = QtWidgets.QPushButton(self.settings)
        self.settingsPMinus1Button.setGeometry(QtCore.QRect(530, 290, 80, 60))
        self.settingsPMinus1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsPMinus1Button.setObjectName("settingsPMinus1Button")
        self.settingsStaticTextLabel = QtWidgets.QLabel(self.settings)
        self.settingsStaticTextLabel.setGeometry(QtCore.QRect(10, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingsStaticTextLabel.setFont(font)
        self.settingsStaticTextLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.settingsStaticTextLabel.setObjectName("settingsStaticTextLabel")
        self.settingsPositionLabel = QtWidgets.QLabel(self.settings)
        self.settingsPositionLabel.setGeometry(QtCore.QRect(190, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingsPositionLabel.setFont(font)
        self.settingsPositionLabel.setStyleSheet("QLabel{\n"
"color : white;\n"
"}")
        self.settingsPositionLabel.setObjectName("settingsPositionLabel")
        self.settingsTipTrashButton = QtWidgets.QPushButton(self.settings)
        self.settingsTipTrashButton.setGeometry(QtCore.QRect(529, 10, 261, 60))
        self.settingsTipTrashButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsTipTrashButton.setObjectName("settingsTipTrashButton")
        self.settingsRightMagnetOffButton = QtWidgets.QPushButton(self.settings)
        self.settingsRightMagnetOffButton.setGeometry(QtCore.QRect(490, 390, 101, 80))
        self.settingsRightMagnetOffButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsRightMagnetOffButton.setObjectName("settingsRightMagnetOffButton")
        self.settingsRightMagnetOnButton = QtWidgets.QPushButton(self.settings)
        self.settingsRightMagnetOnButton.setGeometry(QtCore.QRect(380, 390, 101, 80))
        self.settingsRightMagnetOnButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.settingsRightMagnetOnButton.setObjectName("settingsRightMagnetOnButton")
        self.stackedWidget.addWidget(self.settings)
        self.calibrate = QtWidgets.QWidget()
        self.calibrate.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.calibrate.setObjectName("calibrate")
        self.stackedWidget.addWidget(self.calibrate)
        self.help = QtWidgets.QWidget()
        self.help.setStyleSheet("QWidget\n"
"{\n"
"color : rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
"}")
        self.help.setObjectName("help")
        self.helpInfoTextBrowser = QtWidgets.QTextBrowser(self.help)
        self.helpInfoTextBrowser.setGeometry(QtCore.QRect(10, 13, 781, 341))
        self.helpInfoTextBrowser.setObjectName("helpInfoTextBrowser")
        self.helpBackButton = QtWidgets.QPushButton(self.help)
        self.helpBackButton.setGeometry(QtCore.QRect(0, 360, 801, 120))
        self.helpBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   color : black;\n"
"   \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}")
        self.helpBackButton.setObjectName("helpBackButton")
        self.stackedWidget.addWidget(self.help)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cpBackButton, self.cpNextButton)
        MainWindow.setTabOrder(self.cpNextButton, self.pdBackButton)
        MainWindow.setTabOrder(self.pdBackButton, self.pdSkipButton)
        MainWindow.setTabOrder(self.pdSkipButton, self.pdNextButton)
        MainWindow.setTabOrder(self.pdNextButton, self.vtmBackButton)
        MainWindow.setTabOrder(self.vtmBackButton, self.vtmNextButton)
        MainWindow.setTabOrder(self.vtmNextButton, self.insertBackButton)
        MainWindow.setTabOrder(self.insertBackButton, self.newRunButton)
        MainWindow.setTabOrder(self.newRunButton, self.patientReportButton)
        MainWindow.setTabOrder(self.patientReportButton, self.settingsButton)
        MainWindow.setTabOrder(self.settingsButton, self.helpButton)
        MainWindow.setTabOrder(self.helpButton, self.aboutButton)
        MainWindow.setTabOrder(self.aboutButton, self.insertMainMenuBackButton)
        MainWindow.setTabOrder(self.insertMainMenuBackButton, self.insertOkButton)
        MainWindow.setTabOrder(self.insertOkButton, self.nrPauseButton)
        MainWindow.setTabOrder(self.nrPauseButton, self.nrStopButton)
        MainWindow.setTabOrder(self.nrStopButton, self.exitButton)
        MainWindow.setTabOrder(self.exitButton, self.generatePDFButton)
        MainWindow.setTabOrder(self.generatePDFButton, self.contactInfoTextBrowser)
        MainWindow.setTabOrder(self.contactInfoTextBrowser, self.mainMenuBackButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuamp"))
        self.newRunButton.setText(_translate("MainWindow", "New Run"))
        self.patientReportButton.setText(_translate("MainWindow", "Patient Report"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.helpButton.setText(_translate("MainWindow", "Help"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.mainMenuLabel.setText(_translate("MainWindow", "NUAMP"))
        self.label.setText(_translate("MainWindow", "USB  not Detected"))
        self.cpLabel.setText(_translate("MainWindow", "Choose Program to Run"))
        self.cpBackButton.setText(_translate("MainWindow", "Back"))
        self.cpNextButton.setText(_translate("MainWindow", "Next"))
        self.pdLabel.setText(_translate("MainWindow", "Patient Details"))
        self.pdBackButton.setText(_translate("MainWindow", "Back"))
        self.pdSkipButton.setText(_translate("MainWindow", "Skip"))
        self.pdNextButton.setText(_translate("MainWindow", "Next"))
        self.pdLoadDataButton.setText(_translate("MainWindow", "Load data"))
        self.pdSelectedProgramLabel.setText(_translate("MainWindow", "Selected Program"))
        self.vtmLabel.setText(_translate("MainWindow", "Add VTM Samples on the Deep well"))
        self.vtmBackButton.setText(_translate("MainWindow", "Back"))
        self.vtmNextButton.setText(_translate("MainWindow", "Next"))
        self.vtmSelectedProgramLabel.setText(_translate("MainWindow", "Selected Program"))
        self.insertLabel1.setText(_translate("MainWindow", "Insert the Tip Box and Deep Well in the Nuamp"))
        self.insertBackButton.setText(_translate("MainWindow", "Back"))
        self.insertMainMenuBackButton.setText(_translate("MainWindow", "Main Menu"))
        self.insertOkButton.setText(_translate("MainWindow", "OK"))
        self.insertProgramSelectedLabel.setText(_translate("MainWindow", "Selected Program"))
        self.nrPauseButton.setText(_translate("MainWindow", "Play"))
        self.nrStopButton.setText(_translate("MainWindow", "Stop"))
        self.nrStatusLabel.setText(_translate("MainWindow", "Message"))
        self.nrLabel.setText(_translate("MainWindow", "Nuamp Running"))
        self.nrImageDisplay.setText(_translate("MainWindow", "Display Image here"))
        self.nrProgramSelectedLabel.setText(_translate("MainWindow", "Selected Program"))
        self.nrLabel_2.setText(_translate("MainWindow", "Nuamp Result (Quick View)"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.generatePDFButton.setText(_translate("MainWindow", "Generate PDF"))
        self.nrSaveDataButton.setText(_translate("MainWindow", "save data"))
        self.nrProgramSelectedLabel_2.setText(_translate("MainWindow", "Selected Program"))
        self.contactInfoTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">contact info here</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mainMenuBackButton.setText(_translate("MainWindow", "Back"))
        self.settingsHomeButton.setText(_translate("MainWindow", "Home Device"))
        self.settingsHomeYButton.setText(_translate("MainWindow", "Home Y"))
        self.settingsHomeZButton.setText(_translate("MainWindow", "Home Z"))
        self.settingsYPlus100Button.setText(_translate("MainWindow", "- 100"))
        self.settingsYPlus10Button.setText(_translate("MainWindow", "- 10"))
        self.settingsYPlus1Button.setText(_translate("MainWindow", "- 1"))
        self.settingsLeftMagnetOnButton.setText(_translate("MainWindow", "ENGAGE \n"
"LEFT\n"
"MAGNET"))
        self.settingsBackButton.setText(_translate("MainWindow", "Back"))
        self.settingsYMinus1Button.setText(_translate("MainWindow", "+ 1"))
        self.settingsYMinus10Button.setText(_translate("MainWindow", "+ 10"))
        self.settingsYMinus100Button.setText(_translate("MainWindow", "+ 100"))
        self.settingsYLabel.setText(_translate("MainWindow", "Y"))
        self.settingsZMinus10Button.setText(_translate("MainWindow", "+ 10"))
        self.settingsZPlus100Button.setText(_translate("MainWindow", "- 100"))
        self.settingsZPlus10Button.setText(_translate("MainWindow", "- 10"))
        self.settingsZMinus100Button.setText(_translate("MainWindow", " + 100"))
        self.settingsZLabel.setText(_translate("MainWindow", "Z"))
        self.settingsZPlus1Button.setText(_translate("MainWindow", "- 1"))
        self.settingsZMinus1Button.setText(_translate("MainWindow", " + 1"))
        self.settingsLeftMagnetOffButton.setText(_translate("MainWindow", "DISENGAGE\n"
"LEFT\n"
"MAGNET"))
        self.settingsPAsperateButton.setText(_translate("MainWindow", "PIPETTE \n"
"ASPERATE"))
        self.settingsPDispenseButton.setText(_translate("MainWindow", "PIPETTE \n"
"DISPENSE"))
        self.settingsPMinus100Button.setText(_translate("MainWindow", "+ 100"))
        self.settingsPLabel.setText(_translate("MainWindow", "P"))
        self.settingsPMinus10Button.setText(_translate("MainWindow", "+ 10"))
        self.settingsPPlus10Button.setText(_translate("MainWindow", "- 10"))
        self.settingsPPlus100Button.setText(_translate("MainWindow", "- 100"))
        self.settingsPPlus1Button.setText(_translate("MainWindow", "- 1"))
        self.settingsPMinus1Button.setText(_translate("MainWindow", "+ 1"))
        self.settingsStaticTextLabel.setText(_translate("MainWindow", "Current Position:"))
        self.settingsPositionLabel.setText(_translate("MainWindow", "0"))
        self.settingsTipTrashButton.setText(_translate("MainWindow", "TIP TRASH"))
        self.settingsRightMagnetOffButton.setText(_translate("MainWindow", "DISENGAGE\n"
"RIGHT\n"
"MAGNET"))
        self.settingsRightMagnetOnButton.setText(_translate("MainWindow", "ENGAGE \n"
"RIGHT\n"
"MAGNET"))
        self.helpInfoTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">help section</span></p></body></html>"))
        self.helpBackButton.setText(_translate("MainWindow", "Back"))
