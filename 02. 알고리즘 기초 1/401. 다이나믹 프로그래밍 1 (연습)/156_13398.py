'''
문제
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
단, 수는 한 개 이상 선택해야 한다. 또, 수열에서 수를 하나 제거할 수 있다. (제거하지 않아도 된다)

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 수를 제거하지 않았을 때의 정답은 12+21인 33이 정답이 된다.

만약, -35를 제거한다면, 수열은 10, -4, 3, 1, 5, 6, 12, 21, -1이 되고,
여기서 정답은 10-4+3+1+5+6+12+21인 54가 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
54
'''

# 일단 수를 제거하지 않는 경우는 쉽다.
# 앞수dp+자신 or 자신 중 큰 걸 고르면 되기 때문.

# 하지만 이 문제는 제거가 있다. 경우는 뭐가 있지?
# 자신을 제거하는 경우? 앞 수를 제거하는 경우?
# 그리고 이미 앞에서 제거를 사용했다면 뒤 수에서는 사용불가..

# 앞수dp가 자신보다 작은 상황이 왔을 때 앞앞수dp를 더해볼까?
# 앞앞수dp를 더하는건 한번밖에 사용 못하는거고..
# 가장 중요할 때 사용해야 한다는 것이다.

# 앞수dp가 자신보다 작은 상황이 왔을 때 리스트를 끊어서 저장한다.
# 잘린 리스트들의 max를 구한 리스트를 만들고..
# 거기서 붙어있는 두 수의 합이 가장 큰 것이 답이 될 듯.

# 아니다. 잘린리스트의 맨 오른쪽을 넣어야한다.
# 그래야 하나만 없애고 붙일 수 있다.
# 아니다. 그러면 9 -10 7 -5 -99 8 이런거에서
# [9, 2, 8]이 저장되버린다. 9+7이 빠져버린다.
# 앞 리스트의 top하나전거랑랑 뒤 리스트의 max를 더한다.
'''
n = int(input())

nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]


dp_tops = [0] # 끊긴 리스트의 top-1 dp값을 저장
dp_maxs = [] # 끊긴 리스트의 max dp값들을 저장
temp = 0
for i in range(1, n):
    if nums[i] > nums[i] + dp[i - 1]: # 앞수dp보다 자신이 클 때
        dp_tops.append(dp[i - 2]) # 끊긴 리스트의 top의 전걸 넣는다.
        dp_maxs.append(max(dp[temp : i]))
        temp = i # 어디서 리스트를 끊었는지 초기화

    dp[i] = max(nums[i], nums[i] + dp[i - 1])
dp_maxs.append(max(dp[temp :]))

# print(dp)
# print(dp_tops)
# print(dp_maxs)

answer = 0
for i in range(len(dp_maxs)): # 앞 리스트의 top-1 + 뒤 리스트의 max
    answer = max(answer, dp_maxs[i] + dp_tops[i])

print(answer)
'''
# 밥시간이라 더 점검을 못하고 틀렸습니다를 띄웠다.
# n=2일때 -1000 5같은게 들어오면 어쩔건데..

# 진짜 직관적으로 그냥 잘라진 리스트를 저장하는것도 좋아보인다.
# 밥먹고 와서 하자.
# 제육쌈밥 개맛있네.
'''
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

# print(dp)
# print(dp_tops)
# print(dp_maxs)

# answer = 0 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 답이음수면 어쩌게??
answer = float("-inf")
for i in range(len(dp_maxs)): # 앞 리스트의 top-1 + 뒤 리스트의 max
    answer = max(answer, dp_maxs[i] + dp_tops[i])

print(answer)
'''
# 5 -1 -1 -1 10 -1 -1 20 이게 30이 나온다. 답은 31인데.
# 다 더한 상태에서 음수 하나 생략하면 더 커진다.
# 이걸 빼먹은 것이다.
'''
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

# 이 밑으로는 생략이 없이 최댓값이 나올 경우 음수를 하나 생략해주는 코드
max_with_skip = float("-inf") 
for i in range(n):
    temp = nums[:i] + nums[i+1:]
    temp_dp = [0] * len(temp)
    for j in range(len(temp)):
        if j == 0:
            temp_dp[j] = temp[j]
        else:
            temp_dp[j] = max(temp[j], temp[j] + temp_dp[j-1])
    max_with_skip = max(max_with_skip, max(temp_dp))

answer = max(answer, max_with_skip)

print(answer)
'''
# 된다. 되는 것 같아. 더이상 반례가 없다.
# 그러나 시간 초과네. 이제 여기까지 하고, 진짜 답을 찾으러 가자고.

def main():

    import sys
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int, input().split()))

    dp = [0] * n
    dp_skip = [0] * n

    dp[0] = nums[0]
    dp_skip[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        # 하나가 생략된 경우 + 자신, 자신을 생략
        dp_skip[i] = max(dp_skip[i - 1] + nums[i], dp[i - 1])

    print(max(max(dp), max(dp_skip)))

if __name__ == "__main__":
    main()

# 문제가 너무 복잡하다면, 내가 복잡하게 풀고있는건 아닐지 생각해 보자.