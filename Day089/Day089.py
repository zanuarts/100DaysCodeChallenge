def capitalize(s):
    res = []
    new = ''
    for i in range(len(s)):
        if i%2 == 0:
            new += s[i].upper()
        else:
            new += s[i]
    res.append(new)
    new = ''
    for i in range(len(s)):
        if i%2 == 0:
            new += s[i]
        else:
            new += s[i].upper()
    res.append(new)
    return res

# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!