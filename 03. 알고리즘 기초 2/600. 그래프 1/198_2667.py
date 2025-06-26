'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오.
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''
# 이게 씨발 초등부 1번이라고?
# 그래프라고 생각해보자. 우측이나 아래에 1이 있으면 간선으로 이어진 노드인거지.
# 그렇게 간선들을 다 체크한 graph를 만들고 나서, 연결요소를 찾으면 되는거야.
# 그리고 한 연결요소의 길이도 출력해야하고 말이지.

N = int(input())

MAPs = [list(map(int, input())) for _ in range(N)]

graph = [[] for _ in range(N * N)]

for row in range(N):
    for col in range(N):
        if MAPs[row][col] == 1:
            if col + 1 < N and MAPs[row][col + 1] == 1: # 우측 검사
                graph[row * N + col].append(row * N + (col + 1))
                graph[row * N + (col + 1)].append(row * N + col)
            if row + 1 < N and MAPs[row + 1][col] == 1: # 하단 검사
                graph[row * N + col].append((row + 1) * N + col)
                graph[(row + 1) * N + col].append(row * N + col)

visited = [False] * (N * N)

def dfs(node):
    if visited[node]:
        return 0 # 방문된 애들은 스킵
    
    visited[node] = True
    count = 1 # 하나 방문했으니 재귀당 1카운트
    for neighbor in graph[node]:
        count += dfs(neighbor)
    return count # neighbor들의 재귀카운트가 전부 합해진 값을 반환

answer = []
for i in range(N * N):
    if not visited[i] and MAPs[i // N][i % N]: # 지도에서 1이 표시돼있으면 dfs
        answer.append(dfs(i))

print(len(answer))
print("\n".join(map(str, sorted(answer))))