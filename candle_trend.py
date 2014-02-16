__author__ = 'abc'


def checkDown(valList):
    vclose = valList[0]['close']
    for each in valList:
        if vclose<each['close']:
            return False
        else:
            vclose = each['close']
    # print 'checkDown %d' % len(valList)
    # for each in valList:
    #     print 'date %s - %f' % (each['date'], each['close'])
    return True