'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
'''

# 1 1 1 1 1 1 1 1 1   1   1
#  2  1 1 1 1 1 1 1   8   n-1 / 1
#  2   2  1 1 1 1 1   21  n-2 n-3 / 2*1
#  2   2   2  1 1 1   20  n-3 n-4 n-5 / 3*2*1
#  2   2   2   2  1   5   n-4 n-5 n-6 n-7 / 4*3*2*1
'''
from math import factorial, prod

size = int(input())

answer = 1
for i in range(1, size // 2 + 1):
    A = list(range(size - i, size - i - i, -1))
    B = factorial(i)
    answer += prod(A) // B

print(answer % 10007)
'''
# DP로 푼게 아닌것같은데?

# dp[size]를 2*size 칸의 채울 타일의 경우의 수라고 하면
# 점화식은 dp[size] = dp[size - 1] + dp[size - 2]
# dp[size - 1]은 맨 끝이 세로타일일 때 앞에 채워야 할 타일의 경우의 수
# dp[size - 2]는 맨 끝이 가로타일일 때 앞에 채워야 할 타일의 경우의 수
# 결국 가로 아니면 세로타일로 끝나니까, 이 둘을 더하면 전체 타일의 경우의 수가 된다.

size = int(input())

dp = [0] * (size + 2)
dp[1] = 1
dp[2] = 2

for i in range(3, size + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[size] % 10007)

# 공간 최적화
'''
n = int(input())
a, b = 1, 2

for _ in range(3, n + 1):
    a, b = b, (a + b) % 10007

print(b if n != 1 else a)
'''