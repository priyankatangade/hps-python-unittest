# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestShutdown(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_shutdown_machine(self):
        self.actionwords.press_onoff_button_to_start_the_machine()
        self.actionwords.check_that_machine_is_started()
