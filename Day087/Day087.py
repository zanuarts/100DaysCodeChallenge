def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False

# Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).