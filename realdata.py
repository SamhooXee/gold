__author__ = 'abc'

from candle_trend import checkDown
from candle_reverse import checkChuizi

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
            ret = checkDown(valListRev[i:i+3])
            if ret == True:
                # print valListRev[i]['date']
                ret2 = checkChuizi('down', valListRev[i+3])
                if ret2 == True:
                    print '%s\tChuizi!!!' % (valListRev[i+3]['date'])
                    for each in valListRev[i:i+3]:
                        print '%s - %f' % (each['date'], each['close'])
        except Exception, e:
            print '%d, %s' % (i, e)


