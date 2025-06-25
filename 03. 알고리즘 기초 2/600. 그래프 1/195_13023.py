'''
문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다.
사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b)
같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

예제 입력 1 
5 4
0 1
1 2
2 3
3 4
예제 출력 1 
1
예제 입력 2 
5 5
0 1
1 2
2 3
3 0
1 4
예제 출력 2 
1
예제 입력 3 
6 5
0 1
0 2
0 3
0 4
0 5
예제 출력 3 
0
예제 입력 4 
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
예제 출력 4 
1
'''

# 깊이가 4인게 존재하는지를 찾는거니까 dfs
# 재귀 깊이는 최대 4.

import sys
# sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
found = False

def dfs(node, depth):
    global found

    if node in visited: # 이미 꺼낸거면 스킵
        return
    
    if found: # 이미 찾았으면 스킵
        return
    
    if depth == 4: # 깊이가 4가되면 찾음스위치 켜고 스킵
        found = True
        return
    
    visited.add(node) # 이번에 꺼낸 노드
    for neighbor in graph[node]: # 꺼낸 노드에 이어진 애들
        dfs(neighbor, depth + 1)
    visited.discard(node) # 방문 끝났으면 나가

for i in range(N):
    dfs(i, 0)
    if found:
        break

print(1 if found else 0)