def get_sum(a,b):
    if a == b:
        return b
    else:
        res = 0
        for i in range(min(a,b), max(a,b)+1):
            res += i
            print (res)
        return res

get_sum(0, 1)
get_sum(0, -1)