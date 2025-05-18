'''
입력
입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

출력
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

예제 입력 1 
121
1231
12421
0
예제 출력 1 
yes
no
yes
'''

# 펠린드롬수

import sys
input = sys.stdin.readline

while True:
    num = input().strip() # readline을 쓴다면 절대 strip을 잊어선 안돼
    if num == "0":
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")