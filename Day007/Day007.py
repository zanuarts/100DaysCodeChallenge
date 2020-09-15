def solution(number):
    total = 0
    for n in range (number):
        if n%3 == 0 or n%5 == 0:
            total += n
            print(total)
        else:
            total = total
    print (total)
    return total

print("Multiples of 3 and 5")
print("should handle basic cases")
solution(10)