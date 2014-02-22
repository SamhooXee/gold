__author__ = 'abc'


def checkYunXian(valList):
    v1Max = max(valList[0]['open'], valList[0]['close'])
    v1Min = min(valList[0]['open'], valList[0]['close'])
    v2Max = max(valList[1]['open'], valList[1]['close'])
    v2Min = min(valList[1]['open'], valList[1]['close'])
    if v1Max > v2Max and v1Min < v2Min:
        return True
    return False