def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        sum = begin_number
        gap = begin_number + step
        while gap <= end_number:
            sum += gap
            gap += step
            print(gap)
        print ("sum" , sum)
        return sum

#   "Basic tests"
sequence_sum(2, 6, 2) # 12
sequence_sum(1, 5, 1) # 15
sequence_sum(1, 5, 3) # 5
sequence_sum(0, 15, 3) # 45
sequence_sum(16, 15, 3) # 0
sequence_sum(2, 24, 22) # 26
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 2, 1) # 2
sequence_sum(1, 15, 3) # 35
sequence_sum(15, 1, 3) # 0