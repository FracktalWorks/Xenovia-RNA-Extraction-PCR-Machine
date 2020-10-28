#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Ankit Bhatnagar
 * Created: May 2020
 *
 * Network Related Helper Routines
 *
 * Licence: PROPRIETARY
*************************************************************************
'''
######################
# General
######################
def getIP(interface):
    try:
        scan_result = \
            subprocess.Popen("ifconfig | grep " + interface + " -A 1", stdout=subprocess.PIPE, shell=True).communicate()[0]
        # Processing STDOUT into a dictionary that later will be converted to a json file later
        rInetAddr = r"inet addr:\s*([\d.]+)"
        mtIp = re.search(rInetAddr, scan_result)
        if mtIp and len(mtIp.groups()) == 1:
            return str(mtIp.group(1))
    except:
        return None

def getMac(interface):
    try:
        mac = subprocess.Popen(" cat /sys/class/net/" + interface + "/address",
                               stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not mac:
            return "Not found"
        return mac.upper()
    except:
        return "Error"

def getWifiAp():
    try:
        ap = subprocess.Popen("iwgetid -r",
                              stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not ap:
            return "Not connected"
        return ap
    except:
        return "Error"

def getHostname():
    try:
        hostname = subprocess.Popen("cat /etc/hostname", stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not hostname:
            return "Not connected"
        return hostname + ".local"
    except:
        return "Error"

######################
# WiFi Specific
######################
def acceptWifiSettings(self):
    wlan0_config_file = io.open("/etc/wpa_supplicant/wpa_supplicant.conf", "r+", encoding='utf8')
    wlan0_config_file.truncate()
    ascii_ssid = self.wifiSettingsComboBox.currentText()
    # unicode_ssid = ascii_ssid.decode('string_escape').decode('utf-8')
    wlan0_config_file.write(u"network={\n")
    wlan0_config_file.write(u'ssid="' + str(ascii_ssid) + '"\n')
    if self.hiddenCheckBox.isChecked():
        wlan0_config_file.write(u'scan_ssid=1\n')
    if str(self.wifiPasswordLineEdit.text()) != "":
        wlan0_config_file.write(u'psk="' + str(self.wifiPasswordLineEdit.text()) + '"\n')
    wlan0_config_file.write(u'}')
    wlan0_config_file.close()
    signal = 'WIFI_RECONNECT_RESULT'
    self.restartWifiThreadObject = ThreadRestartNetworking(ThreadRestartNetworking.WLAN, signal)
    self.restartWifiThreadObject.start()
    self.connect(self.restartWifiThreadObject, QtCore.SIGNAL(signal), self.wifiReconnectResult)
    self.wifiMessageBox = dialog.dialog(self,
                                        "Restarting networking, please wait...",
                                        icon="exclamation-mark.png",
                                        buttons=QtGui.QMessageBox.Cancel)
    if self.wifiMessageBox.exec_() in {QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel}:
        self.stackedWidget.setCurrentWidget(self.networkSettingsPage)

def wifiReconnectResult(self, x):
    self.wifiMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
    if x is not None:
        self.wifiMessageBox.setLocalIcon('success.png')
        self.wifiMessageBox.setText('Connected, IP: ' + x)
        self.wifiMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        self.ipStatus.setText(x) #sets the IP addr. in the status bar

    else:
        self.wifiMessageBox.setText("Not able to connect to WiFi")

def networkInfo(self):
    ipWifi = getIP(ThreadRestartNetworking.WLAN)
    ipEth = getIP(ThreadRestartNetworking.ETH)

    self.hostname.setText(getHostname())
    self.wifiAp.setText(getWifiAp())
    if ipEth:
        self.ipStatus.setText(ipEth)
    elif ipWifi:
        self.ipStatus.setText(ipWifi)
    self.wifiIp.setText("Not connected" if not ipWifi else ipWifi)
    self.lanIp.setText("Not connected" if not ipEth else ipEth)
    self.wifiMac.setText(getMac(ThreadRestartNetworking.WLAN))
    self.lanMac.setText(getMac(ThreadRestartNetworking.ETH))
    self.stackedWidget.setCurrentWidget(self.networkInfoPage)

def wifiSettings(self):
    self.stackedWidget.setCurrentWidget(self.wifiSettingsPage)
    self.wifiSettingsComboBox.clear()
    self.wifiSettingsComboBox.addItems(self.scan_wifi())

def scan_wifi(self):
    '''
    uses linux shell and WIFI interface to scan available networks
    :return: dictionary of the SSID and the signal strength
    '''
    # scanData = {}
    # print "Scanning available wireless signals available to wlan0"
    scan_result = \
        subprocess.Popen("iwlist wlan0 scan | grep 'ESSID'", stdout=subprocess.PIPE, shell=True).communicate()[0]
    # Processing STDOUT into a dictionary that later will be converted to a json file later
    scan_result = scan_result.split('ESSID:')  # each ssid and pass from an item in a list ([ssid pass,ssid paas])
    scan_result = [s.strip() for s in scan_result]
    scan_result = [s.strip('"') for s in scan_result]
    scan_result = filter(None, scan_result)
    return scan_result

######################
#Ethernet Specific
######################
def ethSettings(self):
    self.stackedWidget.setCurrentWidget(self.ethSettingsPage)
    # self.ethStaticCheckBox.setChecked(True)
    self.ethNetworkInfo()

def ethStaticChanged(self, state):
    self.ethStaticSettings.setVisible(self.ethStaticCheckBox.isChecked())
    self.ethStaticSettings.setEnabled(self.ethStaticCheckBox.isChecked())
    # if state == QtCore.Qt.Checked:
    #     self.ethStaticSettings.setVisible(True)
    # else:
    #     self.ethStaticSettings.setVisible(False)

def ethNetworkInfo(self):
    txt = subprocess.Popen("cat /etc/dhcpcd.conf", stdout=subprocess.PIPE, shell=True).communicate()[0]

    reEthGlobal = r"interface\s+eth0\s?(static\s+[a-z0-9./_=\s]+\n)*"
    reEthAddress = r"static\s+ip_address=([\d.]+)(/[\d]{1,2})?"
    reEthGateway = r"static\s+routers=([\d.]+)(/[\d]{1,2})?"

    mtEthGlobal = re.search(reEthGlobal, txt)

    cbStaticEnabled = False
    txtEthAddress = ""
    txtEthGateway = ""

    if mtEthGlobal:
        sz = len(mtEthGlobal.groups())
        cbStaticEnabled = (sz == 1)

        if sz == 1:
            mtEthAddress = re.search(reEthAddress, mtEthGlobal.group(0))
            if mtEthAddress and len(mtEthAddress.groups()) == 2:
                txtEthAddress = mtEthAddress.group(1)
            mtEthGateway = re.search(reEthGateway, mtEthGlobal.group(0))
            if mtEthGateway and len(mtEthGateway.groups()) == 2:
                txtEthGateway = mtEthGateway.group(1)

    self.ethStaticCheckBox.setChecked(cbStaticEnabled)
    self.ethStaticSettings.setVisible(cbStaticEnabled)
    self.ethStaticIpLineEdit.setText(txtEthAddress)
    self.ethStaticGatewayLineEdit.setText(txtEthGateway)

def isIpErr(self, ip):
    return (re.search(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ip) is None)

def showIpErr(self, var):
    return dialog.WarningOk(self, "Invalid input: {0}".format(var))

def ethSaveStaticNetworkInfo(self):
    cbStaticEnabled = self.ethStaticCheckBox.isChecked()
    txtEthAddress = str(self.ethStaticIpLineEdit.text())
    txtEthGateway = str(self.ethStaticGatewayLineEdit.text())

    if cbStaticEnabled:
        if self.isIpErr(txtEthAddress):
            return self.showIpErr("IP Address")
        if self.isIpErr(txtEthGateway):
            return self.showIpErr("Gateway")

    txt = subprocess.Popen("cat /etc/dhcpcd.conf", stdout=subprocess.PIPE, shell=True).communicate()[0]
    op = ""

    reEthGlobal = r"interface\s+eth0"
    mtEthGlobal = re.search(reEthGlobal, txt)

    if cbStaticEnabled:
        if not mtEthGlobal:
            txt = txt + "\n" + "interface eth0" + "\n"
        op = "interface eth0\nstatic ip_address={0}/24\nstatic routers={1}\nstatic domain_name_servers=8.8.8.8 8.8.4.4\n\n".format(
            txtEthAddress, txtEthGateway)

    res = re.sub(r"interface\s+eth0\s?(static\s+[a-z0-9./_=\s]+\n)*", op, txt)
    try:
        file = open("/etc/dhcpcd.conf", "w")
        file.write(res)
        file.close()
    except:
        if dialog.WarningOk(self, "Failed to change Ethernet Interface configuration."):
            pass

    signal = 'ETH_RECONNECT_RESULT'
    self.restartEthThreadObject = ThreadRestartNetworking(ThreadRestartNetworking.ETH, signal)
    self.restartEthThreadObject.start()
    self.connect(self.restartEthThreadObject, QtCore.SIGNAL(signal), self.ethReconnectResult)
    self.ethMessageBox = dialog.dialog(self,
                                        "Restarting networking, please wait...",
                                        icon="exclamation-mark.png",
                                        buttons=QtGui.QMessageBox.Cancel)
    if self.ethMessageBox.exec_() in {QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel}:
        self.stackedWidget.setCurrentWidget(self.networkSettingsPage)

def ethReconnectResult(self, x):
    self.ethMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
    if x is not None:
        self.ethMessageBox.setLocalIcon('success.png')
        self.ethMessageBox.setText('Connected, IP: ' + x)
    else:

        self.ethMessageBox.setText("Not able to connect to Ethernet")

def ethShowKeyboard(self, textbox):
    self.startKeyboard(textbox.setText, onlyNumeric=True, noSpace=True, text=str(textbox.text()))