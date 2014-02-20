__author__ = 'abc'

from candle_trend import checkDown
from candle_reverse import checkChuizi, checkShangdiao, checkTunmoRaise, checkTunmoDrop, checkWuYunGaiDing, checkCiTou
from candle_star import checkQiMing, checkHuangHun, checkLiuXing

with open('gold.csv') as f:
    valList = []
    for each in f:
        try:
            valMap = {}
            vals = each.split(',')
            valMap['date'] = vals[0]
            valMap['open'] = float(vals[1])
            valMap['top'] = float(vals[2])
            valMap['down'] = float(vals[3])
            valMap['close'] = float(vals[4])
            valList.append(valMap)
        except Exception, e:
            print each.rstrip()
            print e
    print len(valList)
    print valList[0]
    valListRev = valList[::-1]
    for i in range(0, len(valListRev)):
        try:
            # ret = checkDown(valListRev[i:i+3])
            # if ret == True:
            #     # print valListRev[i]['date']
            #     ret2 = checkChuizi('down', valListRev[i+3])
            #     if ret2 == True:
            #         print '%s\tChuizi!!!' % (valListRev[i+3]['date'])
            #         for each in valListRev[i:i+3]:
            #             print '%s - %f' % (each['date'], each['close'])

            ret =checkTunmoDrop('up', valListRev[i:i+2])
            if ret == True:
                print '%s\tTunmo Drop' % (valListRev[i]['date'])
            ret =checkTunmoRaise('down', valListRev[i:i+2])
            if ret == True:
                print '+++ %s\tTunmo Raise' % (valListRev[i]['date'])
                print valListRev[i:i+2]
            ret =checkWuYunGaiDing('up', valListRev[i:i+2])
            if ret == True:
                print '%s\tWuYunGaiDing' % (valListRev[i]['date'])
            ret =checkCiTou('down', valListRev[i:i+2])
            if ret == True:
                print '+++ %s\tCiTou' % (valListRev[i]['date'])

            ret =checkQiMing('down', valListRev[i:i+3])
            if ret == True:
                print '+++ %s\tQiMing' % (valListRev[i]['date'])
            ret =checkHuangHun('up', valListRev[i:i+3])
            if ret == True:
                print '%s\tHuangHun' % (valListRev[i]['date'])
            ret =checkLiuXing(valListRev[i:i+1])
            if ret == True:
                print '+++ %s\tLiuXing' % (valListRev[i]['date'])

        except Exception, e:
            print '%d, %s' % (i, e)


