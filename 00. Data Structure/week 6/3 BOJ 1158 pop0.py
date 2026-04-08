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

    ##########

    N, K = map(int, input().split())
    Queue = list(range(1, N + 1))

    print("<", end="")
    while len(Queue) != 1:
        for _ in range(K - 1):
            # 최좌측을 최우측으로 보낸다.
            Queue.append(Queue.pop(0))
        print(Queue.pop(0), end=", ")

    print(Queue.pop(0), end=">")

    ##########

    return


# [Review]

# 분명 시간초과가 날 것이다.
# 7164ms; 왜 되냐?


if __name__ == "__main__":
    main()
