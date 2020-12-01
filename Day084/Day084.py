# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 >> [5,4,3,2,1]

def reverse_seq(n):
    res = []
    for i in range (1, n+1):
        res.append(i)
    return res[::-1]