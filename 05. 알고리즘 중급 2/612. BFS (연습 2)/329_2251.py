# Authored by : marigold2003
# Date : 2026-03-05
# Link : https://www.acmicpc.net/problem/2251


import sys

input = sys.stdin.readline


# [Summary] 물통

# 부피가 A(200), B(200), C(200)인 물통이 3개 있다.
# AB는 비어있고, C만 가득 차 있다.

# 다른 물통으로 물을 옮길 수 있다. 과정에서 물의 손실은 없다.
# 단, 한 물통이 비거나 다른 물통이 가득 찰 때까지 물을 부어야 한다.

# 이동은 원하는 만큼 할 수 있다.
# A가 비어 있을 때 C에 담겨있을 수 있는 물의 양을 모두 구해내시오.


def main() -> None:

    # [Ideas]

    # 냄새는 graph 냄새임. 근데 A가 비어있을때, 이게 좀 문젠데...
    # (A, B, C)로 저장해서 graph를 돌리자.
    # visited는 set으로 처리하자. 어차피 범위가 그리 크지 않으니

    # graph 순회. 완전탐색을 해야하겠다.

    ##########

    A, B, C = map(int, input().split())
    answer = set()
    answer.add(C)

    # stack dfs로 순회

    stack = []
    visited = set()

    stack.append((0, 0, C))

    while stack:

        curr = stack.pop()
        if curr in visited:
            continue

        visited.add(curr)

        # a->b 이동에서 옮겨지는 물의 양은 min(a, B빈공간)이 된다.
        a, b, c = curr

        if not a:
            answer.add(c)

        # A를 B와 C에 붓기
        if a:
            stack.append((a - min(a, B - b), b + min(a, B - b), c))
            stack.append((a - min(a, C - c), b, c + min(a, C - c)))

        # B를 A와 C에 붓기
        if b:
            stack.append((a + min(b, A - a), b - min(b, A - a), c))
            stack.append((a, b - min(b, C - c), c + min(b, C - c)))

        # C를 A와 B에 붓기
        if c:
            stack.append((a + min(c, A - a), b, c - min(c, A - a)))
            stack.append((a, b + min(c, B - b), c - min(c, B - b)))

    print(*sorted(answer))

    ##########

    return


# [Review]

# 짜잔! 이제 이정도는 쉽게 풀 수 있다.
# 근데 최적화가 더 되긴 할듯? 물의 총량은 무조건 C니까.
# 3개를 저장하지 않고 c = C-a-b 로 찾는 ab 2차원 visited가 가능해 보임.


if __name__ == "__main__":
    main()
