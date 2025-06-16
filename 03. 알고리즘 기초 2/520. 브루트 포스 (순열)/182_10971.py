'''
문제
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다)
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10)
다음 N개의 줄에는 비용 행렬이 주어진다.
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

예제 입력 1 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
예제 출력 1 
35
'''

# 문제가 길어서 그렇지, 지금까지 해온 것과 다를 게 없다.
# 결국 조합을 찾으라 이거다.

# 1 3 4 2 는 13421순서대로 순회하는 코스인 것이다.
# 중복을 허용하지 않으니 used
# 순열이니까 start는 필요 없고, 요소가 중복될 일도 없으니 prev도 필요없다

# 아, 문제에서 0이 들어오면 막힌 길이라고 했던가??
'''
import sys
input = sys.stdin.readline

N = int(input())
moving_costs = [list(map(int, input().split())) for _ in range(N)]

used = [False] * N
result = []

answer = set()

def backtrack():
    if len(result) == N:
        total_cost = 0
        for i in range(N - 1): # 마지막거만 따로해준다.
            moving_cost = moving_costs[result[i]][result[i + 1]]
            if moving_cost == 0: # 값이 0이면 막힌 길목
                return
            total_cost += moving_cost

        last_cost = moving_costs[result[-1]][result[0]]
        if last_cost == 0: # 마지막 값이 0인지도 따로 확인해주자.
            return
        
        total_cost += last_cost
        answer.add(total_cost)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            result.append(i)
            backtrack()
            result.pop()
            used[i] = False

backtrack()
print(min(answer))
'''
# set()을 사용하지 말고 global로 answer를 초기화하자
# 추가로, 지금 01230 과 12301 을 다 돌고있다. 이건 중복이다.
# 시작점을 정해 놓으면 좀 더 줄일 수 있다.

import sys
input = sys.stdin.readline

N = int(input())
moving_costs = [list(map(int, input().split())) for _ in range(N)]

used = [False] * N
result = []

min_cost = float("inf")

def backtrack():
    global min_cost

    if len(result) == N:
        total_cost = 0
        for i in range(N): # 마지막 반복에 [N-1][0]이 나와야한다.
            moving_cost = moving_costs[result[i]][result[(i + 1) % N]]
            if moving_cost == 0: # 값이 0이면 막힌 길목
                return
            total_cost += moving_cost
    
        min_cost = min(min_cost, total_cost)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            result.append(i)
            backtrack()
            result.pop()
            used[i] = False

# 0번인덱스에서 시작으로 고정함.
used[0] = True
result.append(0)
backtrack()

print(min_cost)
