def high_and_low(numbers):
    nums = numbers.split()
    arr = [int(i) for i in nums]
    low = min(arr)
    high = max(arr)
    return str(high) + " " + str(low)

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") # "542 -214"