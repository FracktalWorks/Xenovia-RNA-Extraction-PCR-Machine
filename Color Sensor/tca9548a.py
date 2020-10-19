

# Load Necessary Modules:
# ----------------------------------------------
import time  # Time access and conversion package
import smbus # I2C bus driver package
import RPi.GPIO as GPIO


# Define the device name and I2C addresses. These are set in the class defintion
# as class variables, making them avilable without having to create a class instance.
#
# The name of this device - note this is private
_DEFAULT_NAME = "TCA9548A"

# Some devices have multiple availabel addresses - this is a list of these addresses (0x70 - 0x77).
# NOTE: The first address in this list is considered the default I2C address for the
# device (0x70).
_AVAILABLE_I2C_ADDRESS = [0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77]


class TCA9548A(object):
    """
    Initialise the TCA9548A chip at ``address`` with ``i2c_driver``.
    :param address:		The I2C address to use for the device.
                        If not provided, the default address is
                        used.
    :param i2c_driver:	An existing i2c driver object. If not
                        provided a driver object is created.
    :return:			Constructor Initialization
                        True-	Successful
                        False-	Issue loading I2C driver
    :rtype:				Bool
    """

    # ----------------------------------------------
    # Device Name:
    device_name = _DEFAULT_NAME

    # ----------------------------------------------
    # Available Addresses:
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # ----------------------------------------------
    # Available Channels:
    available_channels = [0,1,2,3,4,5,6,7]

    # ----------------------------------------------
    # Constructor
    def __init__(self, address=None, debug=None, i2c_driver=None,bus=None,resetPin = None):
        """
        This method initializes the class object. If no 'address' or
        'i2c_driver' are inputed or 'None' is specified, the method will
        use the defaults.
        :param address: 	The I2C address to use for the device.
                            If not provided, the method will default to
                            the first address in the
                            'available_addresses' list.
                                Default = 0x29
        :param debug:		Designated whether or not to print debug
                            statements.
                            0-	Don't print debug statements
                            1-	Print debug statements
        :param i2c_driver:	An existing SMBus driver object.If not parsed, it is created
        :param bus:         bus number of i2c bus on rpi. Defaults to 1 is nothing passed
        :param resetPin:    physical pin connected to reset pin on TCA9548A of RPi in BOARD layout
        """

        # Did the user specify an I2C address?
        # Defaults to 0x70 if unspecified.
        self.address = address if address != None else int(self.available_addresses[0])

        # Load the I2C driver if one isn't provided
        if i2c_driver == None:
            if bus == None:
                self._i2c = smbus.SMBus(1)
            else:
                self._i2c = smbus.SMBus(bus)

            if self._i2c == None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

        # Do you want debug statements?
        if debug == None:
            self.debug = 0  # Debug Statements Disabled
        else:
            self.debug = debug  # Debug Statements Enabled (1)
        if resetPin == None:
            self.resetPin=11
        else:
            self.resetPin = resetPin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.resetPin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setwarnings(False)


    # --------------------------------------------------------------------------
    def is_connected(self):
        """
            Determine if the device is conntected to the system.
            :return: True if the device is connected, otherwise False.
            :rtype: bool
        """
        try:
            self._i2c.read_byte(self.address)
            return True
        except IOError:
            return False


    def enable_channels(self, enable):
        """
        This method enables the connection of specific channels on the
        Qwiic Mux.
        :param enable:		Channel(s) to enable on the Qwiic Mux. Input
                            must be either an individual integer or
                            list. The method will automatically convert
                            an individual integer into a list.
                            Range- 0 to 7
        """
        command = self._i2c.read_byte(self.address)

        # If entry is an integer and not a list; turn it into a list of (1)
        if type(enable) is not list: enable = [enable]

        # Iterate through list
        for entry in enable:
            if type(entry) != int:
                print("TypeError: Entries must be integers.")
            elif entry < 0 or 7 < entry:
                print("Entries must be in range of available channels (0-7).")
            else:
                # Set bit to 1
                command = command | (1 << entry)

        self._i2c.write_byte(self.address, command)

    def disable_channels(self, disable):
        """
        This method disables the connection of specific channels on the
        Qwiic Mux.
        :param enable:		Channel(s) to disable on the Qwiic Mux.
                            Input must be either an individual integer
                            or list. The method will automatically
                            convert an individual integer into a list.
                            Range- 0 to 7
        """
        command = self._i2c.read_byte(self.address)

        # If entry is an integer and not a list; turn it into a list of (1)
        if type(disable) is not list: disable = [disable]

        # Iterate through list
        for entry in disable:
            if type(entry) != int:
                print("TypeError: Entries must be integers.")
            elif entry < 0 or 7 < entry:
                print("Entries must be in range of available channels (0-7).")
            else:
                # Clear bit to 0
                command = command & ~(1 << entry)

        self._i2c.write_byte(self.address, command)

    def enable_all(self):
        """
        This method enables the connection of specific channels on the
        Qwiic Mux.
        """

        # Enable all channels
        self._i2c.write_byte(self.address, 0xFF)

    def disable_all(self):
        """
        This method disables the connection of all channels on the
        Qwiic Mux.
        """

        # Disable all channels
        self._i2c.write_byte(self.address, 0x00)

    def list_channels(self):
        """
        This method lists all the available channels and their current
        configuration (enabled or disabled) on the Qwiic Mux.
        """

        enabled_channels = self._i2c.read_byte(self.address)

        for x in self.available_channels:
            if (enabled_channels & (1 << x)) >> x == 0:
                print("Channel %d: Disabled" % x)
            elif (enabled_channels & (1 << x)) >> x == 1:
                print("Channel %d: Enabled" % x)
            else:
                print("Channel %d: ??? (check configuration)" % x)

