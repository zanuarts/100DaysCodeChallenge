def number(lines):
    if lines == []:
        return []
    out = []
    num = 1
    for line in lines:
        res = str(num) + ": " + line
        out.append(res)
        num += 1
    return out

number([]) # []
number(["a", "b", "c"]) # ["1: a", "2: b", "3: c"]