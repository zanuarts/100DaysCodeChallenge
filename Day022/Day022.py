def encode(st):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in st:
        if x in vowels:
            if x == 'a':
                st = st.replace(x, '1')
            elif x == 'e':
                st = st.replace(x, '2')
            elif x == 'i':
                st = st.replace(x, '3')
            elif x == 'o':
                st = st.replace(x, '4')
            elif x == 'u':
                st = st.replace(x, '5')
    return st
    
def decode(st):
    vowels = ('1', '2', '3', '4', '5')
    for x in st:
        if x in vowels:
            if x == '1':
                st = st.replace(x, 'a')
            elif x == '2':
                st = st.replace(x, 'e')
            elif x == '3':
                st = st.replace(x, 'i')
            elif x == '4':
                st = st.replace(x, 'o')
            elif x == '5':
                st = st.replace(x, 'u')  
    return st

encode('hello') # 'h2ll4'
encode('How are you today?') # 'H4w 1r2 y45 t4d1y?'
encode('This is an encoding test.') # 'Th3s 3s 1n 2nc4d3ng t2st.'
decode('h2ll4') # 'hello'