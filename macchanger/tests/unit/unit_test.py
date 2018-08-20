from unittest import TestCase

from macchanger.mac_changer import MacChanger


class MacChangerTest(TestCase):

    def test_if_mac_changer_obj_can_be_created__Should_return_True(self):
        """"""
        mac_changer = MacChanger(interface="wlan0", mac_address="00:11:22:33:44:55")

        self.assertEqual(mac_changer.interface, "wlan0")
        self.assertEqual(mac_changer.mac_address, "00:11:22:33:44:55")
