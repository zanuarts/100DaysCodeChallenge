def reverseWords(s):
    word_list = s.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence

# Reversed Words