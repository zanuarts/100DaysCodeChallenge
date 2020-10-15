def namelist(names):
    result = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        result = names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names)-1):
            result = result + names[i]['name'] + ", "
        result = result[:-2] + " & " + names[len(names)-1]['name']
    print(result)
    return result

# Format a string of names like 'Bart, Lisa & Maggie'.