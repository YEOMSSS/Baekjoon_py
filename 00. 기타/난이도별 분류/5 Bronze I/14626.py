'''
ISBN = list(input())

total = 0
for i, num in enumerate(ISBN):
    if num == "*":
        continue
    
    num = int(num)
    if i % 2 == 0:
        total += num
    elif i % 2 == 1:
        total += 3 * num


star_index = ISBN.index("*")

mult = 3 if star_index % 2 != 0 else 1

for i in range(10):
    if (i * mult + total) % 10 == 0:
        print(i)
'''

ISBN = input()
total = 0
star_index = ISBN.index("*")

for i in range(13):
    if ISBN[i] == "*":
        continue

    num = int(ISBN[i])
    mult = 1 if i % 2 == 0 else 3
    total += num * mult

star = 1 if star_index % 2 == 0 else 3

for x in range(10):
    if (total + x * star) % 10 == 0:
        print(x)
        break
