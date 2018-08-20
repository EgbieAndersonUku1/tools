import re
import sys
import os
import subprocess
import optparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import macchanger.constants as constants

parser = optparse.OptionParser()


class MacChanger(object):
    """MaCChanger allows the user to change their current MAC address into
       their desired MAC address. This desired use for the program is the command line
       but the user can use the program in whatever manner they desire.

       To use the program at the command line change to current directory and run the follow commands

       Command:
            python mac_changer.py -i <interface> -m <new mac address or modified mac address>

            or

            python mac_changer.py --interface <interface> --mac_address <new mac address or modified mac address>

        Example usage:
            python mac_changer.py -i <wlan0> -m <00:11:22:33:44:55>

       and watch the magic happen.
    """

    def __init__(self, interface, mac_address):
        self.interface = interface
        self.mac_address = mac_address
        self._is_command_line_args_valid()

    def change_mac_address(self):
        """This method when invoked allows the user to change or modify their MAC address"""

        subprocess.call(["ifconfig", self.interface, "down"])
        subprocess.call(["ifconfig", self.interface, "hw", "ether", self.mac_address])
        subprocess.call(["ifconfig", self.interface, "up"])

    @staticmethod
    def get_command_line_args():
        """A static method that returns the arguments used by the user at the command line"""

        parser.add_option("-i", "--interface", dest="interface", help=constants.INTERFACE_HELP)
        parser.add_option("-m", "--mac_address", dest="mac_address", help=constants.MAC_ADDRESS_HELP)
        return parser.parse_args()

    def _is_command_line_args_valid(self):
        """When called checks if the command line arguments entered by the user is valid.
           To qualify as valid the interface and MAC address entered cannot be empty.
        """

        if not self.interface:
            parser.error(constants.SPECIFY_INTERFACE_ERROR)
        elif not self.mac_address:
            parser.error(constants.SPECIFY_MAC_ADDRESS_ERROR)

    def get_current_mac_address(self):
        """Returns the current user MAC address"""

        output_result = subprocess.check_output(["ifconfig", self.interface])
        result = re.search(constants.MAC_ADDRESS_PATTERN, output_result)
        return result.group(0) if result else str(None)

    def is_mac_address_changed(self):
        """Checks if the user MAC address has changed. Returns a successful message if it has
           or failed message if the MAC address failed to change.
        """

        if self.get_current_mac_address() == self.mac_address:
            print(constants.SUCCESSFUL_CHANGED_MAC_ADDRESS.format(self.mac_address))
        else:
            print(constants.FAILED_TO_CHANGE_MAC_ADDRESS_ERROR.format(current_mac_address, self.mac_address))


if __name__ == "__main__":

    # Enables the program to be run from the command line
    options, arguments = MacChanger.get_command_line_args()

    mac_changer = MacChanger(interface=options.interface, mac_address=options.mac_address)
    mac_changer.change_mac_address()

    current_mac_address = mac_changer.get_current_mac_address()
    print("Current MAC address = {}".format(current_mac_address))

    if current_mac_address == 'None':
       print("{}".format(constants.MAC_ADDRESS_ERROR))
    else:
        mac_changer.is_mac_address_changed()
