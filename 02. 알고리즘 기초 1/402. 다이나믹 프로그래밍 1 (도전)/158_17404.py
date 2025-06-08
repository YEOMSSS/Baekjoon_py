'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''
'''
예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
110
예제 입력 2 
3
1 100 100
100 1 100
100 100 1
예제 출력 2 
3
예제 입력 3 
3
1 100 100
100 100 100
1 100 100
예제 출력 3 
201
예제 입력 4 
6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91
예제 출력 4 
208
예제 입력 5 
8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19
예제 출력 5 
253
'''

# 집의 색은 연속되지 않는다.
# 하나 추가로 고려할 부분은, 맨 끝 집끼리도 연속되면 안 된다.
# 선분의 양 끝이 이어져 있다고 생각하면 될 것 같다. 원을 이루는 마을.

# 단순히 순서대로 하다가 마지막에만 틀면 되는 문제가 아니다.
# 첫 집의 색을 정하는 기준이 첫 집의 최솟값이 될 수가 없기에.
# n=3일 때만 봐도 세 집이 다 색이 달라야 하니까.

# 원래였으면 첫집을 일단 최솟값으로 찍고
# 다음 집에서 전집색이 아닌 색 중 최솟값을 더했을 것이다.
# 그런데 이 경우는 첫집색을 정할 수가 없으니
# 세 가지 경우를 다 구해야 쓰겠다.
# 마지막집의 색은 첫집색도 마지막전집색도 아닌색 중 최솟값으로 골라야 하나?

# 음, 그러면 첫 예제에서조차 틀리고 만다.
# 경우를 하나 더 해서, 1-2-...-n의 반대방향으로도 돌려봐야 할 것 같다.

# 진짜 6가지 경우를 다 해봐야겠네, 허참

# 도대체 뭔 소리를 한 거냐?
# 이 문제는 그리디로는 풀 수가 없다. 최솟값으로 찍는다는거부터가 틀려먹었다.
# 똑같은 숫자 나오면 둘중에 어디로 선택할 건데?
# 애초에 전부 구해야하는 문제다. 이 집이 빨초파일때의 최솟값을 전부 각각 저장해야 한단 말이다.

# 1, 2번집을 칠하는 6가지 조합을 고정하고 가야 한다.
# 원래 시작과 마지막을 고정하고 가야하는데, 어차피 원형 마을이라 생각하면 상관없으니까.
'''
import sys

n = int(input())

prices = [list(map(int, val.split())) for val in sys.stdin.read().splitlines()]

dp = [[0, 0, 0] for _ in range(n + 1)]

R, G, B = 0, 1, 2 # 가독성 향상

# 01, 02, 10, 12, 20, 21
starts = [
    [prices[1][R] + prices[0][G], 1001, 1001], [prices[1][R] + prices[0][B], 1001, 1001],
    [1001, prices[1][G] + prices[0][R], 1001], [1001, prices[1][G] + prices[0][B], 1001],
    [1001, 1001, prices[1][B] + prices[0][R]], [1001, 1001, prices[1][B] + prices[0][G]]
]

answer = float("inf")
for index, start in enumerate(starts):
    dp[2] = start
    for i in range(3, n + 1):
        dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + prices[i - 1][R]
        dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + prices[i - 1][G]
        dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + prices[i - 1][B]

    if index == 0 or index == 5: # 시작이 G였을때
        answer = min(min(dp[n][R], dp[n][B]), answer)
    elif index == 1 or index == 3: # 시작이 B였을때
        answer = min(min(dp[n][R], dp[n][G]), answer)
    else: # 시작이 R이었을때
        answer = min(min(dp[n][G], dp[n][B]), answer)
print(answer)
'''
# 씨발 진짜 하기싫게만드네
# 틀렸데 씨발, 뭐 어쩌라는거야

import sys
input = sys.stdin.readline

n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")

answer = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    
    # 첫 번째 집 색 고정
    dp[0][first_color] = prices[0][first_color]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + prices[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + prices[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i][2]
        
    for last_color in range(3):
        if last_color != first_color: # 첫집과 색이 다를때만 answer에 비교해 넣기
            answer = min(answer, dp[n - 1][last_color])

print(answer)

# 한집만 고정해도 되는거라고, 씨발. 씨발. 씨발.