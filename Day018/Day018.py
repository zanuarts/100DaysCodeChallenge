def sum_digits(number):
    num = str(abs(number))
    res = 0
    for item in num:
        res += int(item)
    return res

sum_digits(10) # 1
sum_digits(99) # 18
sum_digits(-32) # 5