__author__ = 'abc'

def checkChuizi(trend, valMap):
    open = valMap['open']
    close = valMap['close']
    down = valMap['down']
    top = valMap['top']
    if trend=='down':
        vmax = max(open, close)
        vmin = min(open, close)
        dif = abs(open - close)
        tail = vmin - down
        head = top - vmax
        # print '%d, %d, %d' % (dif, tail, head)
        if tail > 2*dif:
            if head < dif*0.3:
                print 'dif,%f,head,%f,head/dif,%f' % (float(dif), float(tail), float(head)/float(dif))
                return True
    return False


def checkShangdiao(trend, valMap):
    open = valMap['open']
    close = valMap['close']
    down = valMap['down']
    top = valMap['top']
    if trend=='up':
        vmax = max(open, close)
        vmin = min(open, close)
        dif = abs(open - close)
        tail = vmin - down
        head = top - vmax
        # print '%d, %d, %d' % (dif, tail, head)
        if tail > 2*dif:
            if head < dif*0.3:
                print 'dif,%f,head,%f,head/dif,%f' % (float(dif), float(tail), float(head)/float(dif))
                return True
    return False


def checkTunmoRaise(trend, valList):
    if trend=='down':
        if valList[0]['open'] > valList[0]['close'] and \
            valList[1]['open'] < valList[1]['close'] and \
            valList[0]['open'] < valList[1]['close'] and \
            valList[0]['close'] > valList[1]['open']:
            return True
    return False


def checkTunmoDrop(trend, valList):
    if trend=='up':
        if valList[0]['open'] < valList[0]['close'] and \
            valList[1]['open'] > valList[1]['close'] and \
            valList[0]['open'] > valList[1]['close'] and \
            valList[0]['close'] < valList[1]['open']:
            return True
    return False


def checkWuYunGaiDing(trend, valList):
    if trend=='up':
        if valList[0]['open'] < valList[0]['close'] and \
            valList[1]['open'] > valList[1]['close'] and \
            valList[0]['open'] < valList[1]['close'] and \
            valList[0]['close'] < valList[1]['open'] and \
            (valList[0]['open']+valList[0]['close'])/2 > valList[1]['close']:
            return True
    return False


def checkCiTou(trend, valList):
    if trend=='down':
        if valList[0]['open'] > valList[0]['close'] and \
            valList[1]['open'] < valList[1]['close'] and \
            valList[0]['open'] > valList[1]['close'] and \
            valList[0]['close'] > valList[1]['open'] and \
            (valList[0]['open']+valList[0]['close'])/2 < valList[1]['close']:
            return True
    return False