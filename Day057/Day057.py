def find_it(seq):
    st = 0
    for x in seq:
        if seq.count(x) % 2 != 0 & st != 1:
            return x

# https://github.com/pbldmngz/codewars/blob/master/kyu6/find_odd_int.py