import sys

input = sys.stdin.readline


from math import isqrt


# 1  AB         B1
# 2  AAB
# 3  AAAB
# 4  AABB       B2
# 5  AABAB
# 6  AAABB
# 7  AAABAB
# 8  AAAABB
# 9  AAABBB     B3
# 10 AAABBAB
# 11 AAABABB
# 12 AAAABBB
# 13 AAAABBAB
# 14 AAAABABB
# 15 AAAAABBB
# 16 AAAABBBB   B4

# 일단 B를 isqrt K 개 두고 보면 되겠다.
# 그리고 A를 K // isqrt K한 만큼 왼쪽에 붙이고
# 나머지만큼 B사이에 끼워넣으면 될 듯.


def main() -> None:
    N, K = map(int, input().split())

    if not K:
        print("B" * N)
        return

    Bs = isqrt(K)
    A_left = K // Bs
    A_rest = K % Bs

    # A, B 최소 사용 후 B사이에 남은 짝 위치에 끼워넣기
    if A_rest:
        result = "A" * A_left + "B" * (Bs - A_rest) + "A" + "B" * A_rest
    else:
        result = "A" * A_left + "B" * Bs

    length = len(result)

    if length > N:
        print(-1)
        return

    print("B" * (N - length) + result)


if __name__ == "__main__":
    main()

"""
5 6
1 0
"""


# 문자열의 길이는 상관 없다. 그냥 앞을 B로 다 채우면 되니까.
# 아무거나 출력하면 되니까 ABBBBB로 하면 5개인건가.

# 다만 문자열의 길이가 주어지긴 한다는 것을 봐야 한다.
# A와 B를 가장 적게 사용해서 만든 길이가 주어진 문자열의 길이보다 작으면 성공.
# 곱해서 K를 만드는 두 수의 합이 가장 적도록 하면 된다.

# AABBAB 이거 7이잖아. 애초에 생각을 잘못했다.
# 7*1보다 3*2+1이 더 짧다. 이런 경우는 어쩌지.


def wrong() -> None:

    def min_sum_pair(N):
        root = isqrt(N)  # 정수 sqrt
        for a in range(root, 0, -1):
            if N % a == 0:
                b = N // a
                return a, b, a + b

    N, K = map(int, input().split())

    if not K:
        print("B" * N)
        return

    a, b, a_plus_b = min_sum_pair(K)

    if a_plus_b > N:
        print(-1)
        return

    print("B" * (N - a_plus_b) + "A" * a + "B" * b)
