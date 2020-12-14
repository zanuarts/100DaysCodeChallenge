def palindrome_chain_length(n):
    pal = str(n)[::-1]
    count = 0
    sum = n
    while sum != int(str(sum)[::-1]):
        sum += int(str(sum)[::-1])
        count += 1
    return count