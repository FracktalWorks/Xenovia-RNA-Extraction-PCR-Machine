# Xenovia Color Sensor 

### Main Components:
1. veml6040 colour sensor IC:  [Datasheet](https://www.vishay.com/docs/84276/veml6040.pdf)
2. TCA9548A I2C Switch: [Datasheet](https://www.ti.com/lit/ds/symlink/tca9548a.pdf)

![alt-text](https://github.com/FracktalWorks/Xenovia-RNA-Extraction-PCR-Machine/blob/master/Color%20Sensor/Color%20Sensor%20HW%20Block%20Diagram.png?raw=true "Hardware Architecture")

### Research Links for interfacing:
1. Functionality and example application of TCA9548A [link](https://www.hackster.io/tarantula3/tca9548a-i2c-multiplexer-module-with-arduino-and-nodemcu-3d3313)
2. VEML6040 python example code [link](https://www.raspberrypi.org/forums/viewtopic.php?t=263498)
3. to test detection from raspberry pi and basic understanding of TCA9548A [link](https://www.raspberrypi.org/forums/viewtopic.php?t=146416)
4. Raspberry Pi I2C interfacing Tutorial, detecting connected hardware [link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
### Degugging and Bugs:
#### Hardware:
V1.4
1. Upstream SDA SCL lines on the TCA9548A doesnt not have pullup resistors
2. Diodes on the Raspberry Pi shield need to be reversed due to error in placement from JLCPCB

#### Software:

1. Reset pin on Raspberry Pi is low by default, change to high to prevent resetting the TCA9548A or just disconnect the reset pin.