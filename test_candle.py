from candle_reverse import checkChuizi, checkShangdiao, checkTunmoRaise, checkTunmoDrop, checkWuYunGaiDing, checkCiTou
from candle_trend import checkDown

__author__ = 'abc'

import unittest

class MyTestCase2(unittest.TestCase):
    def test_checkTunmoRaise(self):
        valList = [{'open': 60, 'close': 40, 'top': 80, 'down': 20},
                    {'open': 30, 'close': 70, 'top': 80, 'down': 20}]
        ret = checkTunmoRaise('down', valList)
        self.assertEqual(True, ret)

    def test_checkTunmoDrop(self):
        valList = [{'open': 40, 'close': 60, 'top': 80, 'down': 20},
                    {'open': 70, 'close': 30, 'top': 80, 'down': 20}]
        ret = checkTunmoDrop('up', valList)
        self.assertEqual(True, ret)

    def test_checkWuYunGaiDing(self):
        valList = [{'open': 30, 'close': 70, 'top': 80, 'down': 20},
                    {'open': 80, 'close': 40, 'top': 90, 'down': 20}]
        ret = checkWuYunGaiDing('up', valList)
        self.assertEqual(True, ret)

    def test_checkCiTou(self):
        valList = [{'open': 80, 'close': 40, 'top': 90, 'down': 20},
                    {'open': 30, 'close': 70, 'top': 90, 'down': 20}]
        ret = checkCiTou('down', valList)
        self.assertEqual(True, ret)

class MyTestCase(unittest.TestCase):
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

    def test_checkChuizi1(self):
        valMap = {'open': 100, 'close': 90, 'top': 100, 'down': 10}
        ret = checkChuizi('down', valMap)
        self.assertEqual(True, ret)

    def test_checkChuizi2(self):
        valMap = {'open': 100.0, 'close': 90.0, 'top': 100.0, 'down': 10.0}
        ret = checkChuizi('down', valMap)
        self.assertEqual(True, ret)

    def test_checkShangdiao1(self):
        valMap = {'open': 100, 'close': 90, 'top': 100, 'down': 10}
        ret = checkShangdiao('up', valMap)
        self.assertEqual(True, ret)

if __name__ == '__main__':
    unittest.main()
