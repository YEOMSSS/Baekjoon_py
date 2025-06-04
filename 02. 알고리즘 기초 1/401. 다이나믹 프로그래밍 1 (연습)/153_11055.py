'''
문제
수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에
합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

예제 입력 1 
10
1 100 2 50 60 3 5 6 7 8
예제 출력 1 
113
'''
# 자신으로 끝나는 LIS의 최댓값을 dp에 저장
# 자신보다 작은 애들의 dp값들의 최댓값에 자신을 더해 dp에 저장하면 된다.
'''
import sys
input = sys.stdin.readline

def main():

    n = int(input())

    nums = list(map(int, input().split()))

    dp = [0] * (n + 1)

    dp[1] = nums[0]

    for i in range(2, n + 1):
        for j in range(i - 1):
            if nums[i - 1] > nums[j]:
                dp[i] = max(dp[i], dp[j + 1] + nums[i - 1])

    print(max(dp))

if __name__ == "__main__":
    main()
'''
# 인덱스를 썼다가 순서를 썼다가 하니까 꼬인다..
# 좀 통일하자. 인덱스만 써야겠다.

import sys
input = sys.stdin.readline

def main():

    n = int(input())

    nums = list(map(int, input().split()))

    dp = nums[:] # dp==nums. 굉장히 중요한 부분분

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
                # LIS길이코드에서 +1 대신 +nums[i]를 썼을 뿐.
    
    print(max(dp))
    
if __name__ == "__main__":
    main()
