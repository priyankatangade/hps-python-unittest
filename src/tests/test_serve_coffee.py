# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestServeCoffee(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_simple_use(self):
        # Well, sometimes, you just get a coffee.
        # Tags: priority:high
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I take a  "Expresso" coffee
        self.actionwords.i_take_a_type_coffee(type = "Expresso")
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
