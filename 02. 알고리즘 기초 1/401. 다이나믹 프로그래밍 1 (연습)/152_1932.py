'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다.
삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
'''
# 인덱스가 자신과 같거나 자신+1인 다음줄만 선택 가능.
# 윗줄의 인덱스가 자신인경우 + 자신-1인경우가 자신으로 끝나는경우임.
'''
import sys

n = int(input())

nums = [list(map(int, list(val.split()))) for val in sys.stdin.read().splitlines()]

if n == 1: # 제발이것좀까먹지말고쓰자자
    print(nums[0][0])
    sys.exit()

dp = [[0] * i for i in range(n + 1)]

dp[0] = 0
dp[1] = nums[0]
dp[2] = [nums[0][0] + nums[1][0], nums[0][0] + nums[1][1]]


for i in range(3, n + 1):
    for j in range(i):
        if j > 0: # j==i-1 포함
            dp[i][j] = dp[i - 1][j - 1]

        if j < i - 1: # j==0 포함
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

        dp[i][j] += nums[i - 1][j]
        

print(max(dp[n]))
'''
# 좀 보완할 점이 있다 이거냐?
'''
import sys

n = int(input())
nums = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

if n == 1:
    print(nums[0][0])
    sys.exit()

dp = [[0] * i for i in range(n + 1)]
dp[1][0] = nums[0][0]

for i in range(2, n + 1):
    for j in range(i):
        if j > 0: # left
            dp[i][j] = dp[i - 1][j - 1]
        if j < i - 1: # right
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        dp[i][j] += nums[i - 1][j]

print(max(dp[n]))
'''
# 이젠 main함수를 이용해서 코드를 짜는 연습을 해보자.
'''
import sys

def main():
    n = int(input())
    nums = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

    if n == 1:
        print(nums[0][0])
        return  # main으로 하면 return을 쓸 수 있지.

    dp = [[0] * i for i in range(n + 1)]
    dp[1][0] = nums[0][0]

    for i in range(2, n + 1):
        for j in range(i):
            left = dp[i - 1][j - 1] if j > 0 else 0
            right = dp[i - 1][j] if j < i - 1 else 0
            dp[i][j] = max(left, right) + nums[i - 1][j]

    print(max(dp[n]))

if __name__ == "__main__":
    main()
'''
# 와 이게 공간최적화가 되네

import sys

def main():
    n = int(input())
    nums = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

    if n == 1:
        print(nums[0][0])
        return

    prev = [nums[0][0]]  # 첫줄 하나

    for i in range(1, n):
        curr = [0] * (i + 1)
        for j in range(i + 1):
            left = prev[j - 1] if j > 0 else 0
            right = prev[j] if j < i else 0
            curr[j] = max(left, right) + nums[i][j]
        prev = curr  # 갱신

    print(max(prev))

if __name__ == "__main__":
    main()
