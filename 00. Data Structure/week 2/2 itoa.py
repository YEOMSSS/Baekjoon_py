val = 123231321

temp = val
howmany = 0

while temp:
    howmany += 1
    temp //= 10

data = [0] * howmany

while howmany:
    howmany -= 1
    data[howmany] = str(val % 10)
    val //= 10

print(data)
