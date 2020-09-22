def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    
    result = "*" * n + "\n"
    spaces = 1
    n = n - 2
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current
    
    return result

# expected =  " *\n"
# expected += "***\n"
# expected += " *\n"
diamond(1) # "*\n"
diamond(2) # None
diamond(3) # expected
diamond(5) # "  *\n ***\n*****\n ***\n  *\n"
diamond(0) # None
diamond(-3) # None

#Give up not my ans