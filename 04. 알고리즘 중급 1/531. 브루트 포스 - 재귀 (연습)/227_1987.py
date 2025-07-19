'''
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20)
둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3
예제 입력 2 
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2 
6
예제 입력 3 
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3 
10
'''

# 칸수가 최대 20*20이니까 재귀깊이는 최대 400
# 시간초과 나니까 비트마스크로
# 중복연산 많이되니 캐시 추가. 이게 중요하네

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(N)]

# 4방향 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 중복저장용 캐시, 최대깊이
visited_cache = set()
result = 0

# x좌표, y좌표, 방문확인용 비트, 재귀깊이
def longest_path(x, y, visited, depth):
    global result

    # 중복경로를 피하기 위한 캐시 저장
    # 같은 깊이로 같은 좌표를 가지면 중복임
    key = (x, y, visited)
    if key in visited_cache:
        return
    visited_cache.add(key)

    # 깊이 최댓값 확인
    result = max(result, depth)

    # 4방향에 대해 각각 재귀
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 다음 경로 비트가 켜져있는지 확인하고
        # 꺼져있는 경우에 켜서 재귀
        if 0 <= nx < N and 0 <= ny < M:
            alphabet = ord(maps[nx][ny]) - ord("A")
            if not visited & (1 << alphabet):
                longest_path(nx, ny, visited | (1 << alphabet), depth + 1)

# 시작 알파벳만 켜진 비트마스크로 시작
start = ord(maps[0][0]) - ord("A")
longest_path(0, 0, 1 << start, 1)
print(result)



