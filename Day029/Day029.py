def square_digits(num):
    words = list(str(num))
    res = '' 
    for word in words: 
        numStr = int(word)**2 
        res += str(numStr)
    return int(res)

square_digits(9119) # 811181