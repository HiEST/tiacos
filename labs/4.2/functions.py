import math

def atoi ( ascii_num ):
    val = 0
    for c in ascii_num:
        val = val * 10 + (c - ord('0'))
    return val;

def itoa ( val ):
    c = math.floor(val/100)
    d = math.floor((val-c*100)/10)
    u = val - c*100 - d*10
    ascii_num = "%d%d%d" % (c,d,u)
    return ascii_num.encode();

