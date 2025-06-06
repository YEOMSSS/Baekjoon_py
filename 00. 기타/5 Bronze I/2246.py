'''
import sys

n = int(input())

datas = [list(map(int, val.split())) for val in sys.stdin.read().splitlines()]

ans = 0
for i in range(n):
    temp = True
    for j in range(n):
        if i == j:
            continue
        # 더 가까우면 더 비싸다를 만족 않는 경우 = 더 가까운데 더 싸거나 같음
        # 더 싸면 더 멀다를 만족 않는 경우 = 더 싼데 더 가깝거나 같음. 둘이 합치면?
        if datas[i][0] >= datas[j][0] and datas[i][1] >= datas[j][1]:
            temp = False
            break

    if temp:
        ans += 1

print(ans)
'''
# 너무 반복이 심하고 비효율적.

import sys
input = sys.stdin.readline

n = int(input())
datas = [tuple(map(int, input().split())) for _ in range(n)]

datas.sort() # 거리 오름차순, 거리 같으면 가격 오름차순

min_price = float('inf')
answer = 0

# 정렬이 거리순으로 되어있다.
# 가격이 현 최저가보다 싸다면, 가까운게 더 비싼 조건을 만족한다.
# 그 말은 곧 더 싸면 더 멀다는거다.
for _, p in datas:
    if p < min_price:
        answer += 1
        min_price = p  # 더 싼 가격 갱신

print(answer)

# 머리 존나 아프네 씨발, 좆같네 진짜.