# Authored by : marigold2003
# Date : 2026-02-17
# Link : https://www.acmicpc.net/problem/16953


import sys

input = sys.stdin.readline


# [Summary] A → B


# 가능한 연산은 두 가지이다.
# 1. 2를 곱한다.
# 2. 10을 곱하고 1을 더한다. 그러니까, 1을 오른쪽 끝에 붙인다.

# 정수 A를 B로 바꿔야 한다.
# A를 B로 바꾸기 위한 연산의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 브루트포스로 해결 가능할듯.
    # 연산에 줄어드는 경우는 없기 때문에, B를 넘어가면 커트한다.

    # 아, 근데 굳이 브루트포스로 해야하나?
    # 그냥 bfs 돌리면 되는거 아님?

    # 지금 든 생각이지만 그냥 거꾸로 가면 그리디로도 가능하네.
    # 맨 끝이 1이면 1을 없애고
    # 맨 끝이 짝수면 2로 나누고
    # 맨 끝이 1이 아닌 홀수면 -1을 출력한다.

    ##########

    from collections import deque

    A, B = map(int, input().split())

    queue = deque()
    queue.append(A)

    level = 0
    while queue:
        level += 1

        for _ in range(len(queue)):
            curr = queue.popleft()

            # B를 찾으면 성공, main 종료
            if curr == B:
                print(level)
                return

            # B보다 커지면 실패
            if curr > B:
                continue

            queue.append(curr * 2)
            queue.append(curr * 10 + 1)

    print(-1)

    ##########

    return


# [Review]

# 참 쉽죠잉


if __name__ == "__main__":
    main()
