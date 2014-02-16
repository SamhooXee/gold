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