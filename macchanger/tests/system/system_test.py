import subprocess
from unittest import TestCase
from unittest.mock import patch

from macchanger.mac_changer import MacChanger


class MacChangerSystemTest(TestCase):

    def setUp(self):
        """"""
        self.mac_changer = MacChanger("eth1", mac_address="00:11:22:33:44:55")

    def test_if_change_mac_address_method_is_called(self):

        with patch("macchanger.mac_changer.MacChanger.change_mac_address") as mock_changer:
            self.mac_changer.change_mac_address()
            mock_changer.assert_called()

    def test_if_get_command_line_args_method_is_called(self):

        with patch("macchanger.mac_changer.MacChanger.get_command_line_args") as mock_getter:
            self.mac_changer.get_command_line_args()
            mock_getter.assert_called()

