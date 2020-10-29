def find_short(s):
    sent = s.split()
    l = 999
    for i in sent:
        print(i)
        if len(i) < l:
            l = len(i)
    return l 

# Shortest Word