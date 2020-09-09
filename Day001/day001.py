def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'U', 'E', 'O')
    for x in string:
        if x in vowels:
            string = string.replace(x,"")
            
    print(string)        
    return string

disemvowel("This website is for losers LOL!")