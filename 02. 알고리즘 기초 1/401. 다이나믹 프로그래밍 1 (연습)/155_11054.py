'''
문제
수열 S가 어떤 수 Sk를 기준으로
S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN
을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어,
{10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

예제 입력 1 
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1 
7
힌트
예제의 경우 {1   2     3 4 5 2 1}이 가장 긴 바이토닉 부분 수열이다.
'''

# 일단 증가하는 수열의 길이를 구한 후,
# 거기에서부터 뒤로 감소하는 수열의 길이를 더해 더하면 되겠다.

import sys
input = sys.stdin.readline

def main():

    n = int(input())

    nums = list(map(int, input().split()))

    # 일단 증가하는 수열을 구하자.
    dp_LIS = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp_LIS[i] = max(dp_LIS[i], dp_LIS[j] + 1)

    # nums[i]로 시작해서 감소하는 수열을 구해야 하는데,
    # 뒤집어서 증가하는 수열을 구한 후 다시 뒤집어주면 되겠지.
    nums_rev = nums[::-1]
    dp_LDS = [1] * n

    for i in range(n):
        for j in range(i):
            if nums_rev[i] > nums_rev[j]:
                dp_LDS[i] = max(dp_LDS[i], dp_LDS[j] + 1)

    # 다시 뒤집어서 저장한다.
    dp_LDS = dp_LDS[::-1]

    # nums[i]를 중심으로 앞은 증가, 뒤는 감소하는 수열이다.
    # nums[i]가 겹치니까 -1을 해주면 이어진 수열이 되겠다.
    ans = [dp_LIS[i] + dp_LDS[i] - 1 for i in range(n)]

    print(max(ans))

if __name__ == "__main__":
    main()

# 이제 정말로 LIS에 조금은 익숙해졌구나.
# 풀어냈다! 원콤이다 이거야!
'''
import sys
input = sys.stdin.readline

def main():

    n = int(input())

    nums = list(map(int, input().split()))

    # 일단 증가하는 수열을 구하자.
    dp_LIS = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp_LIS[i] = max(dp_LIS[i], dp_LIS[j] + 1)

    dp_LDS = [1] * n
    # 굳이 nums를 뒤집지 않고 루프를 뒤에서부터 돌려서서 증가하는 수열을 찾는다.
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp_LDS[i] = max(dp_LDS[i], dp_LDS[j] + 1)

    ans = 0
    for i in range(n):
        ans = max(ans, dp_LIS[i] + dp_LDS[i] - 1)

    print(ans)

if __name__ == "__main__":
    main()
'''
# 근데 뭐, [::-1]을 두번 복사하는거랑 시간차이가 크지 않다.
# 그냥 내가 하기에 직관적인게 더 맘에 드네.