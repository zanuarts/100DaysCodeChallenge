def dirReduc(arr):
    opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    res = []
    for i in arr:
        if res and opposite[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(a) # ['WEST'] 
u=["NORTH", "WEST", "SOUTH", "EAST"]
dirReduc(u) # ["NORTH", "WEST", "SOUTH", "EAST"]