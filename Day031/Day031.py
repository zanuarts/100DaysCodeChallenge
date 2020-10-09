def row_sum_odd_numbers(n):
    start = n * (n-1) + 1
    total = 0
    for i in range(n):
        total += start
        start += 2
    return total

row_sum_odd_numbers(1) # 1
row_sum_odd_numbers(2) # 8
row_sum_odd_numbers(13) # 2197
row_sum_odd_numbers(19) # 6859
row_sum_odd_numbers(41) # 68921