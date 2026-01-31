# Authored by : marigold2003
# Date : 2026-01-30
# Link : https://www.acmicpc.net/problem/17088

import sys

input = sys.stdin.readline


# [Summary]

# 최대 10만개의 값으로 이루어진 수열이 들어온다.
# 각 값마다 플마1이 가능할 때, 등차수열을 만들 수 있는가?
# 만들 수 있다면 조정을 몇 번 해야하는지 구해라.


def main():

    # [Ideas]

    # [0]이랑 [1]의 관계만 보면 되는거 아닌가?
    # 1 1, 1 0, 1 -1, 0 1, 0 0, 0 -1, -1 1, -1 0, -1 -1
    # 9가지 경우에 대해서 등차수열을 range로 뽑아서 입력과 1차이면 가능한 case
    # 9가지 다 해보고 가능한 case에 대해 최솟값만 뽑아주면 되겠다.

    ##########

    from itertools import product

    size = int(input())
    arr = tuple(map(int, input().split()))

    if size == 1:
        print(0)
        return

    # 최대 조정 횟수는 10만회
    result = 100_001

    # 9가지 경우 생성
    for d1, d2 in product((-1, 0, 1), repeat=2):

        temp = (arr[1] + d2) - (arr[0] + d1)

        count = 0

        start = arr[0] + d1
        for i in range(size):

            gap = abs(arr[i] - (start + temp * i))

            # 차가 1인 경우 조정 필요
            if gap == 1:
                count += 1
            # 동일한 경우 조정 불필요
            elif gap == 0:
                pass
            # 차가 1보다 크면 조정 불가능
            else:
                break

        else:
            result = min(result, count)

    print(result if result != 100_001 else -1)

    ##########

    return


# [Review]

# 구현도 쉽고 생각하기도 쉬웠던 문제.
# 등차수열이라서 그런지 직관적으로 풀 수 있었다.

if __name__ == "__main__":
    main()
