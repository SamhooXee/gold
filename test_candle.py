from candle_reverse import checkChuizi, checkShangdiao, checkTunmoRaise, checkTunmoDrop, checkWuYunGaiDing, checkCiTou
from candle_star import checkQiMing, checkHuangHun, checkLiuXing
from candle_trend import checkDown

__author__ = 'abc'

import unittest

class TestCaseReverse(unittest.TestCase):
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

class TestCaseTrend(unittest.TestCase):
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

class TestCaseStar(unittest.TestCase):
    def test_checkQiMing(self):
        valList = [{'open': 60, 'close': 40, 'top': 70, 'down': 30},
                    {'open': 20, 'close': 30, 'top': 40, 'down': 10},
                    {'open': 40, 'close': 55, 'top': 60, 'down': 30},]
        ret = checkQiMing('down', valList)
        self.assertEqual(True, ret)

    def test_checkHuangHun(self):
        valList = [{'open': 20, 'close': 40, 'top': 60, 'down': 10},
                    {'open': 50, 'close': 60, 'top': 70, 'down': 40},
                    {'open': 50, 'close': 25, 'top': 60, 'down': 10},]
        ret = checkHuangHun('up', valList)
        self.assertEqual(True, ret)

    def test_checkLiuXing(self):
        valList = [{'open': 20, 'close': 30, 'top': 80, 'down': 17}]
        ret = checkLiuXing(valList)
        self.assertEqual(True, ret)

if __name__ == '__main__':
    unittest.main()
