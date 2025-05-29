# 2157년, 폰 예스이만을 기리기 위해 트라이에슬론이 개최됨.

# a * (d + g) 점수계산
# a = d + g 면 점수에 두배

'''
예제 입력 1 
5
1 0 1
5 2 3
5 5 4
0 1 4
3 7 2
예제 출력 1 
50
'''

import sys
input = sys.stdin.readline

T = int(input())

answers = 0
for _ in range(T):
    a, d, g = map(int, input().split())
    
    score = a * (d + g)
    if a == (d + g):
        score *= 2

    answers = max(answers, score)

print(answers)