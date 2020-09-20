# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestDescaling(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_descaling_needed_after_500_coffees(self):
        # Tags: sprint:4
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # And I handle water tank
        self.actionwords.i_handle_water_tank()
        # And I handle beans
        self.actionwords.i_handle_beans()
        # And I handle coffee grounds
        self.actionwords.i_handle_coffee_grounds()
        # When I take "500" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = "500")
        # Then warning "Coffee warning will be descaled" displayed
        self.actionwords.warning_p1_displayed(p1 = "Coffee warning will be descaled")
