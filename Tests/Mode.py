from collections import Counter

def mode(data):
    numValues = len(data)

    numCount = Counter(data)
    calc_mode = dict(numCount)
    modeResult = [k for k, v in calc_mode.items() if v == max(list(numCount.values()))]

    if len(modeResult) == numValues:
        return
    else:
        return modeResult