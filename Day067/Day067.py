def past(h, m, s):
    hou = h*3600000
    min = m*60000
    sec = s*1000
    res = hou + min + sec
    return res
    