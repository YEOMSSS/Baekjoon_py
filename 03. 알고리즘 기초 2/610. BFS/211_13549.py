'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다.
N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2
힌트
수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.
'''
# bfs + dp로 해보자.

from collections import deque

N, K = map(int, input().split())

dp = [-1] * (100_000 + 1)

queue = deque()
queue.append(N)
dp[N] = 0

# BFS로 최단거리 찾기
while queue:
    current = queue.popleft()
    if current == K:
        break
    # 두배로 순간이동. 이게 제일 빠르기 때문에 제일 먼저 확인해야 한다.
    # 그냥 쌓으면 순위가 밀리니까, appendleft로 최우선으로 확인해준다. 0-1BFS
    # 추가로, 방문된 노드더라도 순간이동을 통해 방문한 게 더 빠를수도 있다. 갱신해야 한다.
    teleport = current * 2
    if teleport <= 100_000 and (dp[teleport] == -1 or dp[teleport] > dp[current]): # 더 빠른게 오면 갱신
        dp[teleport] = dp[current]
        queue.appendleft(teleport)
    # +1칸
    current_plus_1 = current + 1
    if current_plus_1 <= 100_000 and (dp[current_plus_1] == -1 or dp[current_plus_1] > dp[current]):
        dp[current_plus_1] = dp[current] + 1
        queue.append(current_plus_1)
    # -1칸
    current_minus_1 = current - 1
    if 0 <= current_minus_1 and (dp[current_minus_1] == -1 or dp[current_minus_1] > dp[current]):
        dp[current_minus_1] = dp[current] + 1
        queue.append(current_minus_1)

print(dp[K])
# 19 52
# 18 17 16 15 14 13 26 52