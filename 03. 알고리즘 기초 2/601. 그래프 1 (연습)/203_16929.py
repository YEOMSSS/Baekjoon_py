'''
입력
첫째 줄에 게임판의 크기 N, M이 주어진다.
둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다.
게임판은 모두 점으로 가득차 있고, 게임판의 상태는 점의 색을 의미한다.
점의 색은 알파벳 대문자 한 글자이다.

출력
사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.

제한
2 ≤ N, M ≤ 50
예제 입력 1 
3 4
AAAA
ABCA
AAAA
예제 출력 1 
Yes
예제 입력 2 
3 4
AAAA
ABCA
AADA
예제 출력 2 
No
예제 입력 3 
4 4
YYYR
BYBY
BBBY
BBBY
예제 출력 3 
Yes
예제 입력 4 
7 6
AAAAAB
ABBBAB
ABAAAB
ABABBB
ABAAAB
ABBBAB
AAAAAB
예제 출력 4 
Yes
예제 입력 5 
2 13
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
예제 출력 5 
No
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(N)]

# 같은 노드끼리 간선을 잇는다.
graph = [[] for _ in range(N * M)]
for row in range(N):
    for col in range(M):
        current = row * M + col
        # 우측
        if col + 1 < M and maps[row][col] == maps[row][col + 1]:
            right = current + 1
            graph[current].append(right)
            graph[right].append(current)
        # 하단
        if row + 1 < N and maps[row][col] == maps[row + 1][col]:
            down = current + M
            graph[current].append(down)
            graph[down].append(current)

def dfs(start):
    visited = [False] * (N * M)
    distance = [0] * (N * M)

    stack = [start]
    distance[start] = 1
    visited[start] = True

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            distance[neighbor] = distance[current] + 1 # 사이클의 길이를 갱신한다.
            # 다음 경로에 시작이 있는데 길이가 4 이상이면 합격
            if neighbor == start and distance[current] >= 4:
                return True
            
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return False

# 0부터 돌려서 사이클이 있으면 중단
for i in range(N * M):
    answer = dfs(i)
    if answer:
        print("Yes")
        break
else:
    print("No")
