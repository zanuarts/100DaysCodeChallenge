def count_smileys(arr):
    count = 0
    eyes = [':',';']
    nose = ['-','~']
    mouth = [')', 'D']
    
    print(len(arr))
    
    for i, item in enumerate(arr):
        
        if (len(item) == 2):
            if item[0] in eyes and item[1] in mouth:
                count += 1
        elif (len(item) == 3):
            if item[0] in eyes and item[1] in nose and item[2] in mouth:
                count += 1
                
    print (count)        
    return count

# "Basic tests"
count_smileys([]) # 0
count_smileys([':D',':~)',';~D',':)']) # 4
count_smileys([':)',':(',':D',':O',':;']) # 2
count_smileys([';]', ':[', ';*', ':$', ';-D']) # 1