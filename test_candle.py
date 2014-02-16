from candle_reverse import checkChuizi
from candle_trend import checkDown

__author__ = 'abc'

import unittest

class MyTestCase(unittest.TestCase):
    def test_checkChuizi1(self):
        valMap = {'open': 100, 'close': 90, 'top': 100, 'down': 10}
        ret = checkChuizi('down', valMap)
        self.assertEqual(True, ret)

    def test_checkChuizi2(self):
        valMap = {'open': 100.0, 'close': 90.0, 'top': 100.0, 'down': 10.0}
        ret = checkChuizi('down', valMap)
        self.assertEqual(True, ret)

    def test_checkTrend1(self):
        valList = [{'open': 100, 'close': 90, 'top': 100, 'down': 10},
                    {'open': 100, 'close': 80, 'top': 100, 'down': 10},
                    {'open': 100, 'close': 70, 'top': 100, 'down': 10},]
        ret = checkDown(valList)
        self.assertEqual(True, ret)

    def test_checkTrend2(self):
        valList = [{'open': 100, 'close': 90, 'top': 100, 'down': 10},
                    {'open': 100, 'close': 100, 'top': 100, 'down': 10},
                    {'open': 100, 'close': 70, 'top': 100, 'down': 10},]
        ret = checkDown(valList)
        self.assertEqual(False, ret)

if __name__ == '__main__':
    unittest.main()
