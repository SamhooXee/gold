__author__ = 'abc'


def checkQiMing(trend, valList):
    if trend=='down':
        max_2nd = max(valList[1]['open'], valList[1]['close'])
        if valList[0]['open'] > valList[0]['close'] and \
            valList[2]['open'] < valList[2]['close'] and \
            valList[0]['close'] > max_2nd and \
            (valList[0]['open'] + valList[0]['close'])/2 < valList[2]['close']:
            return True
    return False


def checkHuangHun(trend, valList):
    if trend=='up':
        min_2nd = min(valList[1]['open'], valList[1]['close'])
        if valList[0]['open'] < valList[0]['close'] and \
            valList[2]['open'] > valList[2]['close'] and \
            valList[0]['close'] < min_2nd and \
            (valList[0]['open'] + valList[0]['close'])/2 > valList[2]['close']:
            return True
    return False


def checkLiuXing(valList):
    valMax = max(valList[0]['open'], valList[0]['close'])
    valMin = min(valList[0]['open'], valList[0]['close'])
    valMidle = valMax-valMin
    valDown = valMin - valList[0]['down']
    valUp = valList[0]['top'] - valMax
    if valUp >= 3*valMidle and \
        valDown/valMidle < 0.3:
        return True
    return False