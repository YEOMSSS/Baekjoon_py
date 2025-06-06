n = int(input())

nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]


dp_tops = [0] # 끊긴 리스트의 top-1 dp값을 저장
dp_maxs = [] # 끊긴 리스트의 max dp값들을 저장
temp = 0
for i in range(1, n):
    
    dp[i] = max(nums[i], nums[i] + dp[i - 1])

    if nums[i] == dp[i]: # dp가 자신으로 초기화됐을때
        if i >= 2:
            dp_tops.append(dp[i - 2]) # 끊긴 리스트의 top의 전걸 넣는다. 하나 건너뛴 효과
        else:
            dp_tops.append(0)
        dp_maxs.append(max(dp[temp : i]))
        temp = i # 어디서 리스트를 끊었는지 초기화

dp_maxs.append(max(dp[temp :]))

answer = float("-inf")
for i in range(len(dp_maxs)): # 앞 리스트의 top-1 + 뒤 리스트의 max
    answer = max(answer, dp_maxs[i] + dp_tops[i])

print(answer)
