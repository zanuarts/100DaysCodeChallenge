# Highest Scoring Word

def high(x):
    arr,numArr= x.split(' '),[]
    for val in arr:
        intNum = 0
        letters = list(val)
        for word in letters:
            intNum += ord(word) - 96
        numArr.append(intNum)
    return arr[numArr.index(max(numArr))]
        
# https://github.com/yukiflandre/codewars/blob/master/Python/Highest%20Scoring%20Word%206kyu.py

