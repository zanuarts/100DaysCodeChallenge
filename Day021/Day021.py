def reverse_alternate(string):
    
    def reverse(string): 
        string = "".join(reversed(string))
        res.append(string)
        return string 
    
    list = string.split()
    res = []
    for i in range(0, len(list)):
        print(list[i])
        if i%2 == 0:
            res.append(list[i])
        else:
            reverse(list[i])
            
    string = ' '.join([str(elem) for elem in res])
    return string

# "Basic tests"
reverse_alternate("Did it work?") # "Did ti work?"
reverse_alternate("I really hope it works this time...") # "I yllaer hope ti works siht time..."
reverse_alternate("Reverse this string, please!") # "Reverse siht string, !esaelp"
reverse_alternate("Have a beer") # "Have a beer"
reverse_alternate("") # ""