def productFib(prod):
    fib1 = 0
    fib2 = 1
    fib = 0
    res = 0
    con = []
    if res == prod:
        con.append(fib1)
        con.append(fib2)
        con.append(True) 
    else:
        while fib < prod:
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
            print(fib1, fib2)
            if res < prod:
                res = fib1 * fib2
                print (res)
                if res == prod:
                    con.append(fib1)
                    con.append(fib2)
                    con.append(True)
                elif res > prod:
                    con.append(fib1)
                    con.append(fib2)
                    con.append(False)

    return con

test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])