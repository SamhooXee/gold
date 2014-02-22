__author__ = 'abc'

from candle_reverse import checkChuizi, checkShangdiao, checkTunmoRaise, checkTunmoDrop, checkWuYunGaiDing, checkCiTou
from candle_reverse2 import checkYunXian
from candle_star import checkQiMing, checkHuangHun, checkLiuXing
from candle_trend import checkDown, raiseCount, dropCount

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
            retx = checkDown(valListRev[i:i+3])
            if retx == True:
                # print valListRev[i]['date']
                ret = checkChuizi('down', valListRev[i+3])
                if ret == True:
                    cnt = raiseCount(valListRev[i+4:])
                    print '%s\tChuizi!!! - cnt %d' % (valListRev[i+3]['date'], cnt)
                    # for each in valListRev[i:i+3]:
                    #     print '%s - %f' % (each['date'], each['close'])
                # reverse
                ret = checkTunmoRaise('down', valListRev[i+3:i+5])
                if ret == True:
                    cnt = raiseCount(valListRev[i+5:])
                    print '+++ %s\tTunmo Raise - cnt %d' % (valListRev[i]['date'], cnt)
                    print valListRev[i:i+2]
                ret = checkCiTou('down', valListRev[i+3:i+5])
                if ret == True:
                    cnt = raiseCount(valListRev[i+5:])
                    print '+++ %s\tCiTou - cnt %d' % (valListRev[i]['date'], cnt)
                # star
                ret = checkQiMing('down', valListRev[i+3:i+6])
                if ret == True:
                    cnt = raiseCount(valListRev[i+6:])
                    print '+++ %s\tQiMing - cnt %d' % (valListRev[i]['date'], cnt)
                ret = checkLiuXing(valListRev[i+3:i+4])
                if ret == True:
                    cnt = raiseCount(valListRev[i+4:])
                    print '+++ %s\tLiuXing - cnt %d' % (valListRev[i]['date'], cnt)

            # ======================================================
            # # reverse
            # ret = checkTunmoDrop('up', valListRev[i:i+2])
            # if ret == True:
            #     print '%s\tTunmo Drop' % (valListRev[i]['date'])
            # ret =checkWuYunGaiDing('up', valListRev[i:i+2])
            # if ret == True:
            #     print '%s\tWuYunGaiDing' % (valListRev[i]['date'])
            # # star
            # ret =checkHuangHun('up', valListRev[i:i+3])
            # if ret == True:
            #     print '%s\tHuangHun' % (valListRev[i]['date'])

        except Exception, e:
            print '%d, %s' % (i, e)


