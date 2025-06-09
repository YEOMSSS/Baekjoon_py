'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''
'''
예제 입력 1 
3
CCP
CCP
PPC
예제 출력 1 
3
예제 입력 2 
4
PPPP
CYZY
CCPY
PPCC
예제 출력 2 
4
예제 입력 3 
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
예제 출력 3 
4
'''


# 브루트포스 문제라면, 전부 해봐야지.
# 가로로 다 바꿔보고, 세로로 다 바꿔보고.
# 인접한게 제일 긴 경우도 다 찾아봐야겠다.

# 일단 가장 긴게 뭔지 찾는 함수를 작성하자.

import sys
input = sys.stdin.readline

def main():

    def find_max_ans():

        max_cnt = 0

        # 행의 연속 세기
        for i in range(n):
            cnt = 1 
            for j in range(1, n):
                if candy_list[i][j - 1] == candy_list[i][j]:
                    cnt += 1
                else:
                    cnt = 1
                max_cnt = max(max_cnt, cnt) # 들여쓰기에 주의.

        # 열의 연속 세기
        for j in range(n):
            cnt = 1 
            for i in range(1, n):
                if candy_list[i - 1][j] == candy_list[i][j]:
                    cnt += 1
                else:
                    cnt = 1
                max_cnt = max(max_cnt, cnt)

        return max_cnt

    n = int(input())
    candy_list = [list(input().rstrip()) for _ in range(n)]

    answer = find_max_ans()
    # 행의 내부에서 전부 바꿔보기
    for i in range(n):
        for j in range(1, n):
            if candy_list[i][j - 1] != candy_list[i][j]:
                candy_list[i][j - 1], candy_list[i][j] = candy_list[i][j], candy_list[i][j - 1]
                answer = max(answer, find_max_ans())
                candy_list[i][j - 1], candy_list[i][j] = candy_list[i][j], candy_list[i][j - 1]

    # 열의 내부에서 전부 바꿔보기
    for j in range(n):
        for i in range(1, n):
            if candy_list[i - 1][j] != candy_list[i][j]:
                candy_list[i - 1][j], candy_list[i][j] = candy_list[i][j], candy_list[i - 1][j]
                answer = max(answer, find_max_ans())
                candy_list[i - 1][j], candy_list[i][j] = candy_list[i][j], candy_list[i - 1][j]
            
    print(answer)

if __name__ == "__main__":
    main()