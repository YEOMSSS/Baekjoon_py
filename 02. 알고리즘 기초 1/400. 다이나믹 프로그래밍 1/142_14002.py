'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은
A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
10 20 30 50
'''
'''
A_len = int(input())
A_list = list(map(int, input().split()))

dp = [1] * A_len
answer = [[] for _ in range(A_len)]

for i in range(A_len):
    for j in range(i):
        if A_list[j] < A_list[i]:

            if dp[i] < dp[j] + 1:
                answer[i].append(A_list[j])

            dp[i] = max(dp[i], dp[j] + 1)
    answer[i].append(A_list[i])

print(max(dp))
print(*answer[dp.index(max(dp))])
'''
# 역시 단순 append로는 풀 수 없는가
'''
A_len = int(input())
A_list = list(map(int, input().split()))

dp = [1] * A_len
LIS = [[A_list[i]] for i in range(A_len)]

for i in range(A_len):
    for j in range(i):
        if A_list[j] < A_list[i]:

            if dp[i] < dp[j] + 1:
                LIS[i] = LIS[j] + [A_list[i]]

            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# print(LIS)

print(max(dp))
print(*LIS[dp.index(max(dp))])
'''
# 최적화 살짝
'''
A_len = int(input())
A_list = list(map(int, input().split()))

dp = [1] * A_len
LIS = [[A_list[i]] for i in range(A_len)]

for i in range(1, A_len): # dp[0]은 항상 A_list[0]임
    for j in range(i):
        # 이전 숫자가 더 작으면서 이전dp에 1을 더한게 현재dp보다 클 때
        if A_list[j] < A_list[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1 # 현재dp는 이전dp+1이 되고
            LIS[i] = LIS[j] + [A_list[i]] # 현재LIS는 이전LIS+자신이 된다.

max_dp = max(dp)
max_index = dp.index(max_dp)
print(max_dp)
print(*LIS[max_index])
'''
# 역추적?
'''
A_len = int(input())
A_list = list(map(int, input().split()))

dp = [1] * A_len

for i in range(1, A_len):
    for j in range(i):
        if A_list[j] < A_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
idx = dp.index(max_dp)

LIS = []
current = A_list[idx]
length = max_dp

for i in range(idx, -1, -1): # 최대 인덱스에서 0까지 거꾸로간다
    # 거꾸로 보면서 LIS길이가 같으며 수는 더 작은 걸 찾는다.
    if dp[i] == length and A_list[i] <= current:
        LIS.append(A_list[i])
        current = A_list[i] # 현재 수 갱신
        length -= 1 # 길이는 1씩 줄인다.

print(max_dp)
print(*reversed(LIS))
'''
# prev 배열?

# import sys
# input = sys.stdin.readline

A_len = int(input())
A_list = list(map(int, input().split()))

dp = [1] * A_len
prev = [-1] * A_len  # 처음에는 아무것도 없음

for i in range(1, A_len):
    for j in range(i):
        if A_list[j] < A_list[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j  # 자신의 이전 수의 인덱스 기록

max_dp = max(dp)
idx = dp.index(max_dp)

# prev를 이용한 역추적
result = []
while idx != -1:
    result.append(A_list[idx]) # 일단 LIS의 max를 넣고
    idx = prev[idx] # max의 이전 인덱스로 간다.

print(max_dp)
print(*result[::-1])

