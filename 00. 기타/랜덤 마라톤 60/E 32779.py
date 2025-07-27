# 사용한 전력량에 대한 전기 요금은 소수점 절사

import sys
input = sys.stdin.readline

Q = int(input())

for _ in range(Q):
    A, M = map(int, input().split())
    result = A * 1.76 * M / 1000
    print(int(result))
