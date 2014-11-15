#!/usr/bin/env python

import unittest
import mock
from kata import *

class TestKata(unittest.TestCase):
    def setUp(self):
        self.warehouse = mock.Mock()
        self.tpv = TPV(warehouse=self.warehouse)

    def test_in_wh(self):
        self.warehouse.check_exists.return_value = True
        self.warehouse.check_stock.return_value = 30
        result = self.tpv.buy("Product A", 30)
        self.warehouse.check_exists.assert_called_with("Product A")
        self.assertEqual(result, "OK")

    def test_stock_not_enough(self):
        self.warehouse.check_exists.return_value = True
        self.warehouse.check_stock.return_value = 25
        result = self.tpv.buy("Product A", 30)
        self.warehouse.check_stock.assert_called_with("Product A")
        self.assertEqual(result, "KO")

    def test_not_in_wh(self):
        self.warehouse.check_exists.return_value = False
        result = self.tpv.buy("Product B", 25)
        self.assertEqual(result, "KO")




if __name__ == '__main__':
    unittest.main()
