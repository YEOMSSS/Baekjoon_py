'''
문제
스도쿠가 세계적으로 유행이 된 이후에, 비슷한 퍼즐이 매우 많이 나왔다.
게임 매거진 2009년 7월호에는 스도쿠와 도미노를 혼합한 게임인 스도미노쿠가 소개되었다. 

이 퍼즐은 스도쿠 규칙을 따른다.
스도쿠는 9×9 크기의 그리드를 1부터 9까지 숫자를 이용해서 채워야 한다.
스도쿠는 다음과 같은 조건을 만족하게 숫자를 채워야 한다.

각 행에는 1부터 9까지 숫자가 하나씩 있어야 한다.
각 열에는 1부터 9까지 숫자가 하나씩 있어야 한다.
3×3크기의 정사각형에는 1부터 9가지 숫자가 하나씩 있어야 한다.
스도미노쿠의 그리드에는 1부터 9까지 숫자가 쓰여져 있고, 나머지 72칸은 도미노 타일 36개로 채워야 한다.
도미노 타일은 1부터 9까지 서로 다른 숫자의 가능한 쌍이 모두 포함되어 있다.
(1+2, 1+3, 1+4, 1+5, 1+6, 1+7, 1+8, 1+9, 2+3, 2+4, 2+5, ...)
1+2와 2+1은 같은 타일이기 때문에, 따로 구분하지 않는다. 도미노 타일은 회전 시킬 수 있다.
또, 3×3 크기의 정사각형의 경계에 걸쳐서 놓여질 수도 있다.

왼쪽 그림은 퍼즐의 초기 상태를 나타내고, 오른쪽은 퍼즐을 푼 상태이다.
스도미노쿠의 퍼즐의 초기 상태가 주어졌을 때, 퍼즐을 푸는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 채워져 있는 도미노의 개수 N이 주어진다. (10 ≤ N ≤ 35)
다음 N개 줄에는 도미노 하나를 나타내는 U LU V LV가 주어진다.
U는 도미노에 쓰여 있는 한 숫자이고, LU는 길이가 2인 문자열로 U의 위치를 나타낸다.
V와 LV는 도미노에 쓰여 있는 다른 숫자를 나타낸다. 도미노의 위치는 문제에 나와있는 그림을 참고한다.
입력으로 주어지는 도미노의 각 숫자 위치는 항상 인접해 있다.

N개의 도미노의 정보가 주어진 다음 줄에는 채워져 있는 숫자의 위치가 1부터 9까지 차례대로 주어진다.
위치는 도미노의 위치를 나타낸 방법과 같은 방법으로 주어진다.

모든 도미노와 숫자가 겹치는 경우는 없다.

입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 퍼즐에 대해서, 스도쿠를 푼 결과를 출력한다. 항상 답이 유일한 경우만 입력으로 주어진다.
'''
'''
예제 입력 1 
10
6 B2 1 B3
2 C4 9 C3
6 D3 8 E3
7 E1 4 F1
8 B7 4 B8
3 F5 2 F6
7 F7 6 F8
5 G4 9 G5
7 I8 8 I9
7 C9 2 B9
C5 A3 D9 I4 A9 E5 A2 C6 I1
11
5 I9 2 H9
6 A5 7 A6
4 B8 6 C8
3 B5 8 B4
3 C3 2 D3
9 D2 8 E2
3 G2 5 H2
1 A2 8 A1
1 H8 3 I8
8 I3 7 I4
4 I6 9 I7
I5 E6 D1 F2 B3 G9 H7 C9 E5
0
예제 출력 1 
Puzzle 1
872643195
361975842
549218637
126754983
738169254
495832761
284597316
657381429
913426578
Puzzle 2
814267593
965831247
273945168
392176854
586492371
741358629
137529486
459683712
628714935
'''

# 일단 스도쿠 만들기 2580번이랑 유사하다.
# 도미노라는 조건이 하나 더 추가되는 것.
# i를 판단한 후 도미노를 추가로 또 판단해야 한다.
# 도미노를 사용한 걸 set()에 넣어두고 이미 쓴 도미노면 패스해야 한다.
# 도미노를 가로로 놓을지 세로로 놓을지도 판단해야 한다.
# 이번 i가 도미노의 시작일지 끝일지를 판단하면 될 것 같다.

# 원콤. 재밌는 문제네요. 주석 좀만 더 쓰자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import permutations

def sudoku_maker(idx):
    # 재귀깊이가 81회가 되어 모든 스도쿠 칸을 돌면 True를 반환
    if idx == 81:
        return True
    
    # 스도쿠가 이미 차 있으면 다음 인덱스로 실행, 그 결과를 반환
    # False가 반환되면 가장 최근 0으로 돌아가서 다음 i로 넘어가 계속 실행됨
    if sudoku[idx] != 0:
        return sudoku_maker(idx + 1)

    # 3*3네모 인덱스와 가로줄 중복판단 만들기
    row = idx // 9
    col = idx % 9
    square = (row // 3) * 3 + (col // 3)
    sudoku_row = set(sudoku[row * 9 : (row * 9) + 9])
    
    for head, tail in domino_can_use:
        # head부터 스도쿠 판단
        if (
            head not in sudoku_row and
            head not in sudoku_cols[col] and
            head not in sudoku_squares[square]
        ):
            # 스도쿠에 i를 채우고, 세로줄과 3*3네모 중복판단에 i추가
            sudoku[idx] = head
            sudoku_cols[col].add(head)
            sudoku_squares[square].add(head)

            # tail이 오른쪽으로 오는 경우 row는 그대로, col은 +1
            tail_idx = idx + 1
            if col < 8 and sudoku[tail_idx] == 0:
                tail_col = col + 1
                tail_square = (row // 3) * 3 + (tail_col // 3)

                if (
                    tail not in sudoku_row and
                    tail not in sudoku_cols[tail_col] and
                    tail not in sudoku_squares[tail_square]
                ):
                    sudoku[tail_idx] = tail
                    sudoku_cols[tail_col].add(tail)
                    sudoku_squares[tail_square].add(tail)
                    domino_can_use.remove((tail, head))
                    domino_can_use.remove((head, tail))
                    
                    if sudoku_maker(idx + 1):
                        return True
                    
                    sudoku[tail_idx] = 0
                    sudoku_cols[tail_col].remove(tail)
                    sudoku_squares[tail_square].remove(tail)
                    domino_can_use.add((tail, head))
                    domino_can_use.add((head, tail))
            
            # tail이 아래쪽으로 오는 경우 col은 그대로, row는 +1
            tail_idx = idx + 9
            if row < 8 and sudoku[tail_idx] == 0:
                tail_row = row + 1
                tail_square = (tail_row // 3) * 3 + (col // 3)
                sudoku_tail_row = set(sudoku[tail_row * 9 : (tail_row * 9) + 9])

                if (
                    tail not in sudoku_tail_row and
                    tail not in sudoku_cols[col] and
                    tail not in sudoku_squares[tail_square]
                ):
                    sudoku[tail_idx] = tail
                    sudoku_cols[col].add(tail)
                    sudoku_squares[tail_square].add(tail)
                    domino_can_use.remove((tail, head))
                    domino_can_use.remove((head, tail))
                    
                    if sudoku_maker(idx + 1):
                        return True
                    
                    sudoku[tail_idx] = 0
                    sudoku_cols[col].remove(tail)
                    sudoku_squares[tail_square].remove(tail)
                    domino_can_use.add((tail, head))
                    domino_can_use.add((head, tail))
            
            # 되돌려 놓기
            sudoku[idx] = 0
            sudoku_cols[col].remove(head)
            sudoku_squares[square].remove(head)

    # 채울 수 있는 숫자가 없다면 False를 반환
    return False

test = 0
while True:
    test += 1
    N = int(input())
    if N == 0:
        break

    sudoku = [0] * 81
    alphabet = "ABCDEFGHI"
    # 도미노 순열 만들기 (뒤집힌게 중복으로 들어있다. 12 21)
    domino_can_use = set(permutations(range(1, 10), 2))

    # 미리 주어진 도미노 입력받기
    for _ in range(N):
        head, head_coord, tail, tail_coord = input().split()
        head, tail = int(head), int(tail)
        
        head_row = alphabet.index(head_coord[0])
        head_col = int(head_coord[1]) - 1
        sudoku[head_row * 9 + head_col] = head

        tail_row = alphabet.index(tail_coord[0])
        tail_col = int(tail_coord[1]) - 1
        sudoku[tail_row * 9 + tail_col] = tail

        # 사용한 도미노 제거하기
        domino_can_use.remove((head, tail))
        domino_can_use.remove((tail, head))

    filled_nums = list(input().split())
    for num, coord in enumerate(filled_nums):
        row = alphabet.index(coord[0])
        col = int(coord[1]) - 1
        sudoku[row * 9 + col] = num + 1



    # 세로줄, 3*3네모칸 중복체크용 set 리스트
    sudoku_cols = [set() for _ in range(9)]
    sudoku_squares = [set() for _ in range(9)]

    # 중복체크용 set 리스트 채워넣기
    for row in range(9):
        for col in range(9):
            num = sudoku[row * 9 + col]
            if num == 0:
                continue

            # 세로줄에 맞춰서 넣어주기
            sudoku_cols[col].add(num)
            # 스도쿠 사각 틀에 맞춰서 넣어주기
            square = (row // 3) * 3 + (col // 3)
            sudoku_squares[square].add(num)


    # 인덱스 0 부터 순회 시작
    sudoku_maker(0)

    # 완성된 스도쿠 출력
    print(f"Puzzle {test}")
    for row in range(9):
        print("".join(map(str, sudoku[row * 9 : (row * 9) + 9])))
