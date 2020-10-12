def string_transformer(s):
    a = s.split(' ')
    a.reverse()
    result = " ".join(a)
    print(result.swapcase())
    return result.swapcase()

string_transformer("Example string") # "STRING eXAMPLE"
string_transformer("Example Input") # "iNPUT eXAMPLE"
string_transformer("To be OR not to be That is the Question") 
# "qUESTION THE IS tHAT BE TO NOT or BE tO"
# Should handle empty string
string_transformer("") # ""
# Should handle multiple spaces
string_transformer("You Know When  THAT  Hotline Bling") 
# "bLING hOTLINE  that  wHEN kNOW yOU"
# Should handle leading space
string_transformer(" A b C d E f G ") # " g F e D c B a "