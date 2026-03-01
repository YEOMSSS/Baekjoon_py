# Authored by : marigold2003
# Date : 2026-03-01
# Link : https://www.acmicpc.net/problem/2143


import sys

input = sys.stdin.readline


# [Summary] 두 배열의 합

# 배열 A(1K), B(1K)가 주어진다.
# sum(A부분배열) + sum(B부분배열) 이 T가 되는 쌍의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 부분배열의 sum을 모두 구해서 A, B 각각 새로운 배열을 만들자.
    # 한쪽만 sort해서 bsearch로 찾자. 중복 카운트도 잊지 말고.

    # 1208번의 쉬운 버전 느낌? mitm 빼고 다 똑같은 느낌이다.
    # 아, 이어진 부분만 합쳐진다는 점에서 더 편하네. 다만 40이 아니라 1K인게 차이점.
    # 그러면 누적합을 쓰는 편이 좋겠는데? 시작, 끝만 combinations로 뽑자.
    # 이 경우는 그냥 인덱스로 뽑는 편이 더 효율적이겠군.

    # Counter 이새끼 존나 좋잖아??

    ##########

    from itertools import accumulate

    T = int(input())

    # accumulate로 누적합 빠르게 구해주기
    N = int(input())
    A = list(accumulate(map(int, input().split()), initial=0))

    M = int(input())
    B = list(accumulate(map(int, input().split()), initial=0))

    from collections import Counter

    # Counter로 효율적인 관리
    Asum = Counter(A[j] - A[i] for i in range(N + 1) for j in range(i + 1, N + 1))
    Bsum = Counter(B[j] - B[i] for i in range(M + 1) for j in range(i + 1, M + 1))

    answer = 0
    for Aval, Acnt in Asum.items():
        target = T - Aval
        # if target in Bsum:
        answer += Acnt * Bsum[target]

    print(answer)

    ##########

    return


# [Review]

# accumulate도 물론 편하긴 한데
# Counter 이놈 미친 물건이네


if __name__ == "__main__":
    main()
