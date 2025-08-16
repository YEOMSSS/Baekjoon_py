
T = int(input())

for _ in range(T):

    N = int(input())
    nums = list(map(int, input().split()))

    dp = [None] * (N + 1)
    dp[0] = float("-inf")

    for i in range(N):
        dp[i + 1] = max(nums[i], dp[i] + nums[i])
    
    print(max(dp))

# 오랜만에 푸는 기초 dp문제. 완전 까먹진 않아서 다행이다.