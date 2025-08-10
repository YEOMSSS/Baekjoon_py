'''
N = int(input())
result = 0
for i in range(1, N + 1):
    temp = N // i
    if i <= temp:
        result += temp + 1 - i
        

print(result)
'''

import math

N = int(input())

result = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i * j <= N:
            result += 1
        else:
            break

print(result + math.isqrt(N))