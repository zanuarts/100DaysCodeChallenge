def multiplication_table(row,col):
    ret = []
    i = 1
    for j in range(1, row+1):
        res = []
        for k in range(1, row+1):
            i = j*k
            print(i, end= "")
            res.append(i)
        print("\n")
        ret.append(res)
        
    print(ret)
    return ret

multiplication_table(2,2) # [[1,2],[2,4]]
multiplication_table(3,3) # [[1,2,3],[2,4,6],[3,6,9]]