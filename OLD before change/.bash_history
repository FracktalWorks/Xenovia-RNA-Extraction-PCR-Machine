l
ls
rm -rf Downloads Music Public Videos Templates Pictures MagPi
ls
git clone https://github.com/waveshare/LCD
git clone https://github.com/waveshare/LCD-show.git
cd LCD-show/
ls
chmod +x LCD35-show 
./LCD35-show 
sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf 
sudo reboot 
ls
sudo apt install python-pip python-dev python-setuptools python-virtualenv git libyaml-dev build-essential
mkdir OctoPrint && cd OctoPrint
virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install octoprint
exit
cd xenovia/
ls
python3.7 main.py 
nano main.py 
ls
sudo usermod -a -G tty pi
sudo usermod -a -G dialout pi
OctoPrint/venv/bin/octoprint serve
wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.init && sudo mv octoprint.init /etc/init.d
wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.default && sudo mv octoprint.default /etc/default/octoprint
sudo chmod +x /etc/init.d/octoprint
wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.init && sudo mv octoprint.init /etc/init.dsudo chmod +x /etc/init.d/wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.init && sudo mv octoprint.init /etc/init.d/octoprint
wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.init && sudo mv octoprint.init /etc/init.d/octoprint
wget https://github.com/foosel/OctoPrint/raw/master/scripts/octoprint.default && sudo mv octoprint.default /etc/default/octoprint
sudo chmod +x /etc/init.d/octoprint
sudo nano /etc/default/octoprint
sudo update-rc.d octoprint defaults
sudo service octoprint start
ls
nano ~/.bash_aliases
ls
rm -rf tmp/
ls
cd xenovia/
ls
python3.7 main.py 
pip3 install qrcode
python3.7 main.py 
pip3 install websocket
python3.7 main.py 
pip3 install piyaml
pip3 install PyYAML
python3.7 main.py 
pip install pyqt5
sudo apt-get install python3-pyqt5
python3.7 main.py 
suydo python3.7 main.py 
sudo python3.7 main.py 
sudo pip3 install qrcode
sudo pip3 install websocket
sudo pip3 install PyYAML
sudo python3.7 main.py 
cd xenovia/
ls
cat main.py 
python3.7 main.py 
ython3.7 main.py 
python3.7 main.py 
ls
cp config/config_printer.yaml /home/pi/.octoprint/config.yaml 
cat /home/pi/.octoprint/config.yaml
cp -f config/config_printer.yaml /home/pi/.octoprint/config.yaml 
cat /home/pi/.octoprint/config.yaml
sudo service octoprint restart
sudo service octoprint
sudo service octoprint status
ping xenovia.local
sudo /etc/init.d/haproxy restart
sudo service octoprint status
sudo /etc/init.d/haproxy stop
sudo service octoprint stop
sudo service octoprint start
ifconfig
netstat
curl http://localhost:5000
sudo reboot 
sudo service octoprint status
~/Octoprint/bin/octoprint config set --bool server.allowFraming true
pwd
ls
~/OctoPrint/bin/octoprint config set --bool server.allowFraming true
~/OctoPrint/venv/bin/octoprint config set --bool server.allowFraming true
sudo service octoprint restart
sudo service octoprint status
~/OctoPrint/venv/bin/octoprint serve
~/Octoprint/bin/octoprint config set --bool server.allowFraming false
~/OctoPrint/venv/bin/octoprint config set --bool server.allowFraming false
ls
cd .octoprint/
ls
cat config.backup 
ls
cp config.backup config.yaml 
~/OctoPrint/venv/bin/octoprint serve
sudo service octoprint start
sudo service octoprint status
sudo service octoprint restart
sudo service octoprint status
ls
cd p
cd printerProfiles/
ls
cat _default.profile 
cd ..
cat config.yaml 
ls
cat printerProfiles/xenovia.profile 
cp printerProfiles/xenovia.profile /home/pi/xenovia/config/config_printer.yaml 
cat config.yaml | grep xenovia
cp config.yaml /home/pi/xenovia/config/config_octoprint.yaml
sudo shutdown -h now
nano .octoprint/config.yaml 
cd xenovia/
python3.7 main.py 
sudo nano /etc/lightdm/lightdm.conf
sudo cp /etc/lightdm/lightdm.conf /etc/lightdm/lightdm.backup
sudo nano /etc/lightdm/lightdm.conf
sudo reboot
sudo apt purge libpam-chksshpwd
sudo reboot
xhost +local:pi
export DISPLAY=:0.0
d xenovia/
cd xenovia/
python3.7 main.py 
cd xenovia/
python3.7 main.py 
export DISPLAY=:0.0
python3.7 main.py 
dmesg
dmesg | grep tty
udevadm info -a -p  $(udevadm info -q path -n /dev/ttyUSB0)
udevadm info --name=/dev/ttyUSB0 --attribute-walk
udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep idVendor
udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep idProduct
udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep SerialNumber
udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep SerialNumbers
lsusb
udevadm info -a -n /dev/ttyUSB0 | grep '{serial}'
cd /etc/udev/
cd rules.d/
ls
cat 99-com.rules 
sudo nano 99-usb-serial.rules
sudo cat 99-usb-serial.rules
udevadm control --reload-rules && udevadm trigger.
sudo udevadm control --reload-rules && udevadm trigger.
sudo udevadm control --reload-rules && udevadm trigger
udevadm control --reload-rules
sudo udevadm control --reload-rules
sudo udevadm trigger --attr-match=subsystem=net
ls /dev/
pwd
sudo reboot
ls
cd xenovia/
ls
cd ../LCD-show/
ls
sudo ./LCD-hdmi 
cd xenovia/
export DISPLAY=:0.0
python3.7 main.py 
cd xenovia/ui/
git pull
git branch 
ls
ls -a
rm *
ls
git clone git@bitbucket.org:karthikramx/nuampui.git
git clone https://ankitmcgill@bitbucket.org/karthikramx/nuampui.git
ls
ls nuampui/
cd ..
rm -rf ui/
git clone https://ankitmcgill@bitbucket.org/karthikramx/nuampui.git ui
cd ui/
git checkout UI-changes 
ls
cd ..
vim classes/MainUI.py 
nano classes/MainUI.py 
export DISPLAY=:0.0
python3.7 main.py 
nano main.py 
python3.7 main.py 
nano classes/MainUI.py 
ls yu
ls ui
nano classes/MainUI.py 
python3.7 main.py 
cd ui
ls
                                                                                                                                                                                                                          wifi
wifi status
ls
rm -rf xenovia
mv xenovia_new/ xenovia
ls
cd xenovia/
./run.sh 
ls
mkdir log
touch xenovia.log
ls
mv xenovia.log log/
ls
./run.sh 
cd ..
ls
ls xenovia_new/
rm -rf xenovia_new/
ls
pwd
cd /lib/systemd/system
;s
ls
sudo nano xenovia.service
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
/usr/bin/python3.7 /home/pi/xenovia/main.py 
export DISPLAY=:0.0
/usr/bin/python3.7 /home/pi/xenovia/main.py 
pwd
/usr/bin/python3.7 /home/pi/xenovia/main.py 
sudo systemctl status xenovia.service 
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo pip3 install parse
sudo systemctl status xenovia.service 
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo pip3 install pandas
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo nano xenovia.service
sudo systemctl start xenovia.service 
systemctl daemon-reload
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo nano xenovia.service
sudo systemctl start xenovia.service 
systemctl daemon-reload
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo nano xenovia.service
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo nano xenovia.service
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
nano ~/xenovia/run.sh 
chmod a+x $!
chmod a+x ~/xenovia/run.sh 
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo systemctl daemon-reload
sudo systemctl start xenovia.service 
sudo systemctl status xenovia.service 
sudo systemctl stop xenovia.service 
sudo reboot
cd xenovia/
ls
pwd
nano run.sh 
sudo systemctl status xenovia.service 
journalctl 
journalctl -u xenovia.service
journalctl -u xenovia
cat /var/log/syslog
sudo systemctl stop xenovia.service 
sudo nano ~/.config/lxsession/LXDE/autostart
mkdir -p ~/.config/autostart
nano ~/.config/autostart/xenovia.desktop
sudo reboot
cat /lib/systemd/system/xenovia.service
sudo systemctl disable xenovia.service
sudo systemctl status xenovia.service
sudo reboot
cd xenovia/
ls
nano tests/TestBase.py 
git status
git diff classes/MainUI.py
git status
git diff main.py
git status
git status run.sh 
git diff run.sh
git status
git checkout .
git status

ls
cd ui/
ls
rm popup1.ui popup2.ui xenovia_ui.*
ls
rm Main.py 
ls
cd ..
nano tests/TestCovid19/
nano tests/TestCovid19/TestCovid19.py 
./ run.sh
./run.sh
nano tests/TestCovid19/TestCovid19.py 
./run.sh
nano classes/TipHolderTray.py 
./run.sh
nano classes/MainUI.py 
nano tests/TestTipPickTrash/TestTipPickTrash.py 
./run.sh
killall xinitrc
killall xinit
sudo nano
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
sudo reboot
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
sure reboot
sudo reboot
ifconfig wlan0
ifconfig eth0
ifconfig wlan0
ifconfig wlan1
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
sudo reboot
ls
cd xenovia/
ls
git status
micro
curl https://getmic.ro | bash
ls
git status
./micro 
ls
cd ..
mv xenovia/micro .
./micro ~/.bash_aliases 
. ~/.bash_aliases
micro
cat ~/.bash_aliases 
ls
micro
exit
micr
nano ~/.bash_aliases 
. ~/.bash_aliases
micro
cd xenovia/
gs
git diff classes/MechanicalParameters.py
git log
gs
git diff tests/TestCovid19/TestCovid19.py
git diff classes/Magnet.py
git add classes/Magnet.py classes/MechanicalParameters.py tests/TestCovid19/TestCovid19.py
gd
gs
git branch 
git checkout -b feature/ankit/fw_changes_new
git dif --cached classes/MechanicalParameters.py
git diff --cached classes/MechanicalParameters.py
micro classes/MechanicalParameters.py 
gs
git diff classes/Magnet.py
git diff --cached classes/Magnet.py
git branch 
git checkout feature/ankit/basic_working_fw 
exit
cd xenovia/
gs
micro
gs
git diff classes/MechanicalParameters.py
git add classes/MechanicalParameters.py 
git commit -m "temp commit"
git push origin 
exit
micro /etc/rc.local 
sudo micro /etc/rc.local
sudo nano /etc/rc.local 
sudo dpkg-reconfigure x11-common 
sudo nano /etc/X11/Xsession.options 
dpkg-reconfigure x11-common 
sudo dpkg-reconfigure x11-common 
sudo apt-get install xserver-xorg-legacy
sudo dpkg-reconfigure x11-common 
cat /etc/X11/Xwrapper.config 
sudo nano  /etc/X11/Xwrapper.config 
cat /etc/X11/Xwrapper.config 
sudo nano ~/.xinitrc
sudo reboot 
rm ~/.xinitrc 
sudo nano /etc/X11/xinit/xinitrc 
sudo reboot 
cd ~
nano .xinitrc
cat .xinitrc
nano /etc/X11/xinit/xinitrc 
ls xenovia/
pws
pwd
sudo nano /etc/X11/xinit/xinitrc
sudo reboot 
startx
sudo nano /etc/X11/xinit/xinitrc 
sudo chmod 755 ~/.xinitrc 
cat ~/.xinitrc
sudo reboot 
cat /etc/rc.local 
sudo nano /etc/rc.local 
sudo reboot 
cat /var/log/syslog
cat /var/log/syslog | grep xorg
startx
sudo chmod +x /etc/rc.local 
sudo systemctl enable rc-local.service
sudo reboot 
sudo nano /etc/rc.local
sudo nano /etc/X11/xinit/xinitrc 
sudo reboot 
sudo nano /etc/X11/xinit/xinitrc 
sudo chmod a+x 755 /etc/rc.local 
sudo chmod a+x /etc/rc.local
sudo reboot 
cat /var/log/syslog
cat /var/log/syslog | grep xinit
cat /var/log/syslog | grep xorg
cat /var/log/syslog | grep x11
cat /var/log/syslog | grep startx
cat /var/log/syslog | grep xenovia
cat /var/log/syslog | grep main
cat /var/log/Xorg.0.log
cat /etc/rc.local 
sudo nano /etc/rc.local
sudo reboot 
ps - ax | grep python
ps -ax | grep python
sudo nano /etc/rc.local
sudo nano /etc/X11/xinit/xinitrc 
nano ~/.xinitrc 
sudo reboot 
cd xenovia/
ls
mkdir others
cd others/
sudo nano auto_startup.md
cd ..
gs
git diff main.py
git add others/
gs
git commit -m "added others folder to house references & links"
g
gs
git push origin 
sudo reboot 
cd xenovia/
micro others/auto_startup.md 
cd others/
l
echo $USER
sudo chmod a+w auto_startup.md
ll
;
l
mv auto_startup.md references.md
cd ..
gs
git add others/auto_startup.md
git add others/references.md
gs
git commit -m "renamed references file"
git push origin
ps -ax| grep python
sudo kill -9 489
startx
pwd
exit
ls
mv fracktal_logo.png splash.png
l
ls temp/
rm -rf temp/
l
sudo cp splash.png /usr/share/plymouth/themes/pix/splash.png 
sudo nano /usr/share/plymouth/themes/pix/pix.script 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
pw
pwd
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo nano /boot/config.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
sudo nano /boot/cmdline.txt 
sudo reboot 
xsetroot 
man xsetroot 
sudo apt-get install xsetbg
sudo reboot 
ls
cd xenovia/
./run.sh 
startx
;ps -ax | grep python
ps -ax | grep python
sudo kill -9 492
python3 xenovia/main.py 
cd xenovia/
./run.sh 
sudo reboot 
nano xenovia/others/references.md 
sudo nano /etc/X11/xorg.conf
sudo reboot 
cd xenovia/
micro others/references.md 
history
sudo cp ~/FW_\ 800X480.jpg /usr/share/plymouth/themes/pix/splash.png
sudo reboot 
ls
rm FW_\ 800X480.jpg 
sudo cp ~/FW_\ 800X480.png /usr/share/plymouth/themes/pix/splash.png
sudo reboot 
ls
mv FW_\ 800X480.png fracktal_splash.png
ll
l
rm splash.png 
l
pwd
cd xenovia/
micro classes/MechanicalParameters.py 
cd xenovia/
gs
git diff classes/MechanicalParameters.py
git diff classes/Pipette.py
git add classes/Pipette.py classes/MechanicalParameters.py 
gs
git commit -m "updated pipette levels vs axis mapping as per levels given by Ganesh"
gs
git add others/references.md
git commit -m "updated references document"
git push origin 
python3 xenovia/main.py 
cd xenovia/
python3 xenovia/main.py 
ls
python3 main.py 
export DISPLAY=:0.0
cd /home/pi/xenovia
python3.7 main.py
reboot
sudo reboot
./run.sh 
ps -as| get python
ps -ax| get python
ps -ax| grep python
sudo kill -9 491
ls
cd xenovia/
gs
git diff main.py
git checkout -- main.py
gs
python3 main.py 
./run.sh 
sudo journalctl -u
journalctl -u
journalctl
sudo reboot 
sudo reboot
./run.sh 
startx
cd xenovia/
gs
\gp
gp
git pull
sudo reboot
startx
cd xenovia/
git pull
sudo reboot
startx
nano xenovia/tests/TestCovid19/TestCovid19.py 
sudo reboot
startx
nano xenovia/tests/TestCovid19/TestCovid19.py 
nano xenovia/tests/TestBase.py 
startx
cd xenovia/
gs
git checkout -- tests/TestBase.py
git pull
startx
nano classes/Magnet.py 
startx
nano classes/Magnet.py 
vim classes/Magnet.py
startx
nano tests/TestCovid19/TestCovid19.py 
exit
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot

startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
                                                                                                                                          micro /boot/config.txt 
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo micro /boot/config.txt 
sudo reboot 
sudo micro /boot/config.txt 
sudo reboot 
cd xenovia/
gs
git diff classes/MechanicalParameters.py
gs
git diff classes/MainUI.py
git stash
git pull
git stash pop
micro classes/MechanicalParameters.py
startx
micro classes/MechanicalParameters.py
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
cd xenovia/
lc
ls
cd tests
ls
cd TestCovid19
ls
nano TestCovid19.py
nano /home/pi/xenovia/classes/MechanicalParameters.py
sudo reboot
nano /home/pi/xenovia/classes/MechanicalParameters.py
cd /home/pi/xenovia/
ls
cd tests
ls
cd TestCovid19
ls
nano TestCovid19.py
startx
nano TestCovid19.py
startx
ls
cd xenovia
ls
cd tests
ls
cd TestCovid19
ls

nano TestCovid19.py
cd tests
cd  tests
cd--
cd -
ls
cd TestPumpingAction
ls
nano TestPumpingAction.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
startx
nano /home/pi/xenovia/classes/MechanicalParameters.py
