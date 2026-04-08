# Authored by : marigold2003
# Date : 2026-04-08
# Link : https://www.acmicpc.net/problem/1158


import sys

input = sys.stdin.readline


# [Summary] 요세푸스 문제

# 1 ~ N(<= 5K)번까지 사람이 원형으로 앉아있다.
# 순서대로 K번째 사람을 제거한다.


def main() -> None:

    # [Ideas]

    # 리스트를 만들어서 pop(0) 후 append하고,
    # K번째마다 pop(0)만 해서 출력하는 방법을 사용해 보자.

    # 이번엔 deque로 Queue를 만들어서
    # popleft를 사용하자.

    # 이번엔 deque에서 rotate를 사용하자.

    ##########

    from collections import deque

    N, K = map(int, input().split())
    dq = deque(range(1, N + 1))

    result = []

    while len(dq) != 1:
        # K-1만큼 덱을 왼쪽으로 보낸다.
        dq.rotate(-(K - 1))
        result.append(dq.popleft())

    result.append(dq.popleft())

    print("<", end="")
    # print(", ".join(map(str, result)))
    print(*result, sep=", ", end="")
    print(">")

    ##########

    return


# [Review]

# 파이썬이 좋긴 좋아.


if __name__ == "__main__":
    main()
