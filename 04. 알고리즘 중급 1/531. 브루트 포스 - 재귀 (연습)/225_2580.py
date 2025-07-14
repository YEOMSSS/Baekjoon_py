'''
문제
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.



나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다.
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

예제 입력 1 
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
예제 출력 1 
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''
# 스도쿠에서 확인해야 할 것?
# 가로, 세로, 3*3 네모칸.
# 네모칸이 좀 까다로운데, 미리 잘라놓는게 편하려나...

import sys

# 기본 스도쿠 배열 입력받기
sudoku = list(map(int, sys.stdin.read().split()))

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

def sudoku_maker(idx):
    # 재귀깊이가 81회가 되어 모든 스도쿠 칸을 돌면 True를 반환
    if idx == 81:
        for row in range(9):
            print(*sudoku[row * 9 : (row * 9) + 9])
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
    
    for i in range(1, 10):
        # 스도쿠에 들어갈 수 있는 숫자일 때만 재귀 실행
        # 가로줄, 세로줄, 3*3네모에서 각각 중복판단
        if (
            i not in sudoku_row and
            i not in sudoku_cols[col] and
            i not in sudoku_squares[square]
        ):
            # 스도쿠에 i를 채우고, 세로줄과 3*3네모 중복판단에 i추가
            sudoku[idx] = i
            sudoku_cols[col].add(i)
            sudoku_squares[square].add(i)

            # 실행 후 깊이81을 찍고 True가 반환되면 재귀 종료
            if sudoku_maker(idx + 1):
                return True
            
            # 되돌려 놓기
            sudoku[idx] = 0
            sudoku_cols[col].remove(i)
            sudoku_squares[square].remove(i)

    # 채울 수 있는 숫자가 없다면 False를 반환
    return False

# 인덱스 0 부터 순회 시작
sudoku_maker(0)
