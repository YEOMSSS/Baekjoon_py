# 자기 약수만큼 열렸다 닫혔다를 반복할 것..
# 약수가 짝수면 닫히고, 약수가 홀수면 열린다.
# 약수가 홀수개 있으려면, 제곱수일때뿐 아닌가?
'''
N = int(input())

X = 1
result = 0
while X ** 2 <= N:
    result += 1
    X += 1
print(result)
'''

from math import isqrt

N = int(input())
result = isqrt(N)

print(result)