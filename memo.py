import math

def prime_judge(val):
    if val < 2:
        return False
    for i in range(2, int(math.sqrt(val)) + 1): # 제곱근에는 내림을 해주자.
        if val % i == 0:
            return False
    return True
'''
num = int(input())
for i in range(1, num + 1):
    if prime_judge(i):
        print(i, end = " ")
'''
print(prime_judge(101))