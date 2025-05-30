'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
'''
'''
T = int(input())

nums = list(map(int, input().split()))

num_max = 0
answer = 0
for num in nums:
    if num > num_max:
        num_max = num # 가장 큰 수 저장
        answer += 1
print(answer)
'''
# 시원하게 틀린 코드다. 10 1 2 3 4 5를 입력받고 1을 출력하는 머저리 코드
# dp로 풀어야 한다.

T = int(input())

nums = list(map(int, input().split()))

dp = [1] * T
# dp[i]는 nums[i]를 마지막 원소로 갖는 가장 긴 증가하는 부분 수열의 길이.

for i in range(T):
    for j in range(i):
        if nums[j] < nums[i]: # nums[i]가 더 크면
            # nums[j]에 1을 더한 값과 현재 dp[i]값을 비교해 큰 걸 취한다.
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
# print(dp)

# 나중에 이분탐색으로 더 쉽게 할수 있다고 한다.