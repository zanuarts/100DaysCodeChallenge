def likes(names):
    if (len(names) == 0):
        return "no one likes this"
    else:
        for n in names:
            if (len(names) == 1):
                return str(names[0]) + " likes this"
            elif (len(names) == 2):
                return str(names[0]) + " and " + str(names[1]) + " like this"
            elif (len(names) == 3):
                return str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
            else:
                return str(names[0]) + ", " + str(names[1]) + " and " + str(len(names)-2) + " others like this"

likes([]) # 'no one likes this'
likes(['Peter']) # 'Peter likes this'
likes(['Jacob', 'Alex']) # 'Jacob and Alex like this'
likes(['Max', 'John', 'Mark']) # 'Max, John and Mark like this'
likes(['Alex', 'Jacob', 'Mark', 'Max']) # 'Alex, Jacob and 2 others like this'