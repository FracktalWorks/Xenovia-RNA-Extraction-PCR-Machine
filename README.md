# Xenovia RT-PCR Machine

Ankit Bhatnagar
ankit.bhatnagarindia@gmail.com

Vijay Raghav Varada
vjvarada@fracktal.in

## Firmware Architecture

![alt-text](https://github.com/FracktalWorks/Xenovia-RNA-Extraction-PCR-Machine/blob/master/Doccumentation%20&%20Resources/Firmware%20Structure.png?raw=true "Firmware Architecture")

## Firmware Functional Block Diagram
![alt-text](https://github.com/FracktalWorks/Xenovia-RNA-Extraction-PCR-Machine/blob/master/Doccumentation%20&%20Resources/Code%20Functional%20Block%20Diagram.png?raw=true "Firmware Functional BLock Diagram")

* `main_window` in main.py is an object of `MainUI` class that is the workhorse for the firmware.
* `MainUI` class is the main workhorse. Using getter methods the `Printer` class and `Tests` class is parsed into the `MainUI` class. `xenovia.ui` is inherited by `MainUI` class.
* `xenovia_ui` is the generated code from the `xenovia_ui.ui` file made in Qt Designer and then converted into python code using PyQt5 UI code generator 5.14.2 .
* `Printer` class is Abstracts the Gcode calls to the control board connected over USB and presents an API that is used by `tests` and `MainUI` etc for printer movement functionality.
* `MKSCheck` creates the connection to the printer over USB.
* `MKSSerialCommunication` class handles the communication to the printer. its initialised by the `Printer` class.
* `Tests` is the class that manages available tests, listing them, parsing their class object to `MainUI` etc.
* tests folder contains the assays which are dynamically initialised into `MainUI` by `Tests` class. each Assay class inherits `TestBase` class.
* `TestBase` contains methods common to all Assays.
* When an assay class in dynamically created into `MainUI` by `Tests`, the base function movement classes of `Pipette`, `TipTrash`, `Magnet` etc which have motion related medhods are passed into it.
* `MechanicalParameters` has all the dimenttions of the accessories in the machine, that the base function movement classes of `Pipette`, `TipTrash`, `Magnet` etc uses.

### Research Links:


## Xenovia Color Sensor 

### Main Components:
1. veml6040 colour sensor IC:  [Datasheet](https://www.vishay.com/docs/84276/veml6040.pdf)
2. TCA9548A I2C Switch: [Datasheet](https://www.ti.com/lit/ds/symlink/tca9548a.pdf)

![alt-text](https://github.com/FracktalWorks/Xenovia-RNA-Extraction-PCR-Machine/blob/master/Doccumentation%20&%20Resources/Color%20Sensor%20HW%20Block%20Diagram.png?raw=true "Hardware Architecture")

### Research Links for interfacing:
1. Functionality and example application of TCA9548A [link](https://www.hackster.io/tarantula3/tca9548a-i2c-multiplexer-module-with-arduino-and-nodemcu-3d3313)
2. VEML6040 python example code [link](https://www.raspberrypi.org/forums/viewtopic.php?t=263498)
3. To test detection from raspberry pi and basic understanding of TCA9548A [link](https://www.raspberrypi.org/forums/viewtopic.php?t=146416)
4. Raspberry Pi I2C interfacing Tutorial, detecting connected hardware [link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
5. SMBus [link](http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc)
### Degugging and Bugs:
#### Hardware:
V1.4
1. Upstream SDA SCL lines on the TCA9548A doesnt not have pullup resistors, uses internal pullups on the raspberry pi board
2. Diodes on the Raspberry Pi shield need to be reversed due to error in placement from JLCPCB

#### Software:

1. Reset pin on Raspberry Pi is low by default, change to high to prevent resetting the TCA9548A or just disconnect the reset pin.


## Xenovia Application Auto Startup References

### X Server + Xenovia Application Autostart
1. https://www.raspberrypi.org/forums/viewtopic.php?t=42888
2. https://www.websences.com/dpkg-reconfigure-x11-common/
3. https://github.com/raspberrypi/linux/issues/2517#issuecomment-387867933

1. global xinitrc file : /etc/X11/xinit/xinitrc (set permissin a+x)
2. pi user .xinitrc file : /home/pi/.xinitrc (set permission a+x)
3. global rc.local file : /etc/rc.local (set permission a+x)

### Removing Logo And Initial Boot Stuff

1. https://www.raspberrypi.org/forums/viewtopic.php?t=189666
2. https://www.raspberrypi.org/forums/viewtopic.php?t=236647
3. https://www.thedigitalpictureframe.com/customize-your-raspberry-pi-splash-screen-raspbian-stretch-april-2019-version/
4. https://github.com/raspberrypi/linux/issues/2517#issuecomment-3878679334
5. https://raspberrypi.stackexchange.com/questions/59310/remove-boot-messages-all-text-in-jessie

### Execution Flow
```rc.local ---> startx ---> global .xinitrc ---> pi user .xinitrc ---> xenovia program```
