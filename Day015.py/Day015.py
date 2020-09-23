def is_pangram(s):
    print(s)
    letter = set()
    for character in s:
        if character.isalpha():
            letter.add(character.lower())
    if len(letter) == 26:
        return True
    else:
        return False

# Test
pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram(pangram) # True