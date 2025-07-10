# 작은 수부터 정렬해서 상대할 수 있도록 하면 된다.

import sys
input = sys.stdin.readline

N = int(input())
P, *attacks = map(int, input().split())

attacks = sorted(attacks)

for attack in attacks:
    if P > attack:
        P += attack
    else:
        print("No")
        break
else:
    print("Yes")