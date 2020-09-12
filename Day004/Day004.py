def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

is_isogram("Dermatoglyphics") # True
is_isogram("isogram") # True
is_isogram("aba") # False
is_isogram("moOse") # False
is_isogram("isIsogram") # False
is_isogram("") # True