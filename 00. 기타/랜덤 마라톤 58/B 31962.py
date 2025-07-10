# 아니 씨.. 왤케 문제 이해하기가 어려워??

import sys
input = sys.stdin.readline

N, X = map(int, input().split())

result = -1
for _ in range(N):
    S, T = map(int, input().split())

    if S + T <= X:
        result = max(result, S)

print(result)