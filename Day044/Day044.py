# https://github.com/AlekseiAQ/codewars-py/blob/master/solutions/kyu_6/persistent_bugger.py

from functools import reduce

def persistence(n):
    nums = [int(x) for x in str(n)]
    p = 0
    while len(nums) > 1:
        new_nums = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(new_nums)]
        p += 1
    return p