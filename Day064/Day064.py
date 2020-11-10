def solve(s):
    low = 0
    up = 0
    for char in s:
        if char.isupper() == True:
            up += 1
        else:
            low += 1
    if low > up:
        return s.lower()
    elif low < up:
        return s.upper()
    else:
        return s.lower()

# Fix string case