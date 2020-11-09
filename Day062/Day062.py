def dig_pow(n, p):
    x = 0
    for i,j in enumerate(str(n)):
        x += pow(int(j), p + i)
    return x/n if x%n==0 else -1