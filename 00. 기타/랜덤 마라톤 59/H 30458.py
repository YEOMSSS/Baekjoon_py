# 왼쪽이랑 오른쪽의 내용물이 같으면 된다.
# 아, 꼭 같은게 아니라 다 더해서 모든 문자가 짝수개 있으면 되는구나.

from collections import Counter

import sys
input = sys.stdin.readline

N = int(input())

string = input().rstrip()
if N % 2 == 1:
    string = string[: N // 2] + string[N // 2 + 1 :]

char_count = Counter(string)

odd_count = 0
for value in char_count.values():
    if value % 2 == 1:
        odd_count += 1

if odd_count ==0:
    print("Yes")
else:
    print("No")
