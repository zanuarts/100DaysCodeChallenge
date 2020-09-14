def open_or_senior(data):
    res = []
    for n in data:
        if n[0] >= 55 and n[1] > 7:
            res.append('Senior')
        else:
            res.append('Open')
    return res

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]) # ['Open', 'Senior', 'Open', 'Senior']
open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]) # ['Open', 'Open', 'Senior', 'Open']