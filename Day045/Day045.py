# Maximum subarray sum

def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for i in arr:
        current_sum+=i # 1
        if current_sum < 0: # 2
            current_sum = 0
        else:
            max_sum = max(max_sum, current_sum) # 3
             
    return max_sum

# https://nostacktofullstack.com/2020/09/01/codewars-maximum-subarray-sum/