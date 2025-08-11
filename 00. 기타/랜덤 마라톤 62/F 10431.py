'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    no, *students = map(int, input().split())

    temp_list = []
    moves = 0
    for s in students:
        idx = 0

        while idx < len(temp_list) and temp_list[idx] < s:
            idx += 1

        moves += len(temp_list) - idx
        temp_list.insert(idx, s)

    print(no, moves)
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    no, *students = map(int, input().split())
    moves = 0

    # 버블 정렬: 앞 사람보다 작으면 자리 바꿈
    for i in range(len(students)):
        for j in range(len(students)-1):
            if students[j] > students[j+1]:
                students[j], students[j+1] = students[j+1], students[j]
                moves += 1

    print(no, moves)

# 왜 결과가 같은거지? 전혀 다른 시뮬레이션인 것 같은데... 신기하네.