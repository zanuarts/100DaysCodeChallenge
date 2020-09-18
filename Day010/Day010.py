def duplicate_count(text):
    lower = text.lower()
    dupli = 0
    chara = {}
    
    for i in range (0,len(lower)):
        chara [lower[i]] = 0
    
    for key in chara:
        for i in range(0, len(lower)):
            if (key == lower[i]):
                chara[key] = chara[key] + 1
                
    for key in chara:
        if (chara[key] > 1):
            dupli = dupli +1
    
    print (chara)
    return dupli

duplicate_count("abcde") # 0
duplicate_count("abcdea") # 1
duplicate_count("indivisibility") # 1