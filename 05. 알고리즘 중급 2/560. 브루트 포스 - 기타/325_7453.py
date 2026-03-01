# Authored by : marigold2003
# Date : 2026-03-01
# Link : https://www.acmicpc.net/problem/7453


import sys

input = sys.stdin.readline


# [Summary] 합이 0인 네 정수

# 정수로 이루어진 크기(4K)가 같은 배열 A, B, C, D가 있다.
# A[a], B[b], C[c], D[d]의 합이 0인
# (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

# 특이사항: 제한시간 12초


def main() -> None:

    # [Ideas]

    # 일단 지금까지 풀어온 문제들과의 연관성이 느껴진다.
    # AB로 합배열 만들고, CD로 합배열 만들고.
    # 한쪽만 sort해서 bsearch로 탐색하고.
    # 중복카운팅 left right로 잘 해주고.

    # 시간을 많이 주니까 4K*4K = 16M 도 잘 하겠지.

    # 음, 이번엔 Counter를 사용해보고 싶은데...
    # 뭔가 초과가 날 거 같음. 제출을 한번 해보긴 해야겠다.

    # 둘 다 시간초과네, 투포인터를 쓰는 수밖에.

    ##########

    N = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    ##########

    # Counter 사용 버전

    from collections import Counter

    ABsum = Counter()
    for i in range(N):
        for j in range(N):
            ABsum[A[i] + B[j]] += 1

    answer = 0

    for i in range(N):
        for j in range(N):
            target = -(C[i] + D[j])

            answer += ABsum[target]

    print(answer)

    # bsearch 사용 버전
    """
    from bisect import bisect_left, bisect_right

    # ABsum = list(A[i] + B[j] for i in range(N) for j in range(N))
    CDsum = list(C[i] + D[j] for i in range(N) for j in range(N))
    CDsum.sort()

    answer = 0
    for i in range(N):
        for j in range(N):
            target = -(A[i] + B[j])
            left = bisect_left(CDsum, target)
            right = bisect_right(CDsum, target)

            answer += right - left

    print(answer)
    """

    # two pointer 사용 버전
    """
    ABsum = list(A[i] + B[j] for i in range(N) for j in range(N))
    CDsum = list(C[i] + D[j] for i in range(N) for j in range(N))
    ABsum.sort()
    CDsum.sort()

    p1 = 0
    p2 = len(CDsum) - 1
    answer = 0

    size = len(ABsum)

    while p1 < size and p2 >= 0:
        s = ABsum[p1] + CDsum[p2]

        # 조건 만족 시 중복 확인하기
        if s == 0:
            AB_val = ABsum[p1]
            CD_val = CDsum[p2]

            AB_cnt = 0
            while p1 < size and ABsum[p1] == AB_val:
                p1 += 1
                AB_cnt += 1

            CD_cnt = 0
            while p2 >= 0 and CDsum[p2] == CD_val:
                p2 -= 1
                CD_cnt += 1

            answer += AB_cnt * CD_cnt

        # target보다 작으면 키운다.
        elif s < 0:
            p1 += 1
        # target보다 크면 줄인다.
        else:
            p2 -= 1

    print(answer)
    """

    ##########

    return


# [Review]

# 일단 Counter는 메모리초과가 좀 무서우니까...
# bsearch로 먼저 제출해봅시다.

# bsearch 시간초과? 일단 Counter를 내보기나 할까..
# 역시 시간초과, 결국 투포인터를 써야겠다.

# 투포인터로 통과. 근데 진짜 Counter로 안돼?


if __name__ == "__main__":
    main()
