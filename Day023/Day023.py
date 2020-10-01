letters = [chr(ascii) for ascii in range(65, 91)] # ascii letters

def rot13(message):
    res = ""
    for char in message:
        char_up = char.upper()
        try:
            pos = letters.index(char_up)
            rot13 = letters[(pos+13)%26]
            rot13 = rot13.lower() if char.islower() else rot13
            res += rot13
        except:
            res += char
    return res

rot13("test") # "grfg"
rot13("Test") # "Grfg"