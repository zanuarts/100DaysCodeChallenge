def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
            
    return result

array_diff([1,2], [1]) # [2], "a was [1,2], b was [1], expected [2]"
array_diff([1,2,2], [1]) # [2,2], "a was [1,2,2], b was [1], expected [2,2]"
array_diff([1,2,2], [2]) # [1], "a was [1,2,2], b was [2], expected [1]"
array_diff([1,2,2], []) # [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]"
array_diff([], [1,2]) # [], "a was [], b was [1,2], expected []"