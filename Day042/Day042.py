def tribonacci(signature, n):
    if n<1:
        return []
    if n<len(signature):
        return signature[0:n] 
    inc = 0
    seq = signature[:]
    while inc<=n:
        add = sum(seq[inc:inc+3])
        seq.append(add)
        inc += 1
    return seq[0:n]

# learn from here https://ao.gl/solving-tribonacci-sequence-with-python/