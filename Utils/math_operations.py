def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)
