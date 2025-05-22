def gcd_maker(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd_maker(20, 10))