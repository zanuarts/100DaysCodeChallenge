def descending_order(num):
    s = sorted([i for i in str(num)], reverse=True)
    return int("".join(s))

descending_order(0) # 0
descending_order(15) # 51
descending_order(123456789) # 987654321