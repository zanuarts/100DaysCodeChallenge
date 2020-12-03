def reverse_words(text):
    s = text.split(" ")
    newWord = [i[::-1] for i in s]
    res = " ".join(newWord)
    return res

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"