import sys

input = sys.stdin.readline


# 최대입력: 보석 30만개, 가방 30만개
# 가장 큰 가방에 가장 비싸면서 큰 보석을 넣어야 한다. 가능한 한?
# 어차피 한 가방에 보석이 무겁든 비싸든 하나밖에 못들어간다.
# 그러면 값어치가 많이 나가는 걸 우선으로 챙겨야 한다. 무게당 값어치를 구하자.
# 어차피 한 가방에 하나인데 무게당 값어치를 구할 필요가 있나? 흠...
# 최대한 작은 가방에 최대한 비싼 걸 넣는 식으로 가보자.


# 최대힙을 사용해보자. 자료구조기초 시간이군.
# 파이썬의 heapq는 최소힙만 제공하므로 -를 붙여서 최대힙으로 사용한다.
import heapq


def main() -> None:
    # 보석 개수, 가방 개수
    N, K = map(int, input().split())
    # 각 보석 무게, 각 보석 가격
    juwels = [tuple(map(int, input().split())) for _ in range(N)]
    # 각 가방에 담을 수 있는 최대 무게
    bags = [int(input()) for _ in range(K)]

    # 보석은 무게기준 오름차순으로 정렬
    juwels.sort(key=lambda x: x[0])
    bags.sort()

    # 최고 가격의 보석을 계속 처리하면 되니까 최대 힙을 사용한다.
    max_heap = []
    total = 0

    # 무게기준 오름차순 정렬된 보석리스트의 인덱스
    j = 0

    for bag in bags:
        # 이번 가방에 들어갈 수 있는 보석을 전부 최대힙에 밀어넣는다.
        # 이번 가방에 들어갈 수 있는 보석이 다음 가방에 무조건 들어갈 수 있다는 것을 이용한다.
        while j < N and juwels[j][0] <= bag:
            # 힙에 음수로 push해준다.
            heapq.heappush(max_heap, -juwels[j][1])
            j += 1

        # 힙이 차 있다면, 이번 가방에 넣을 가장 비싼 보석을 힙에서 꺼낸다.
        if max_heap:
            # 힙에서 꺼낸 수의 부호를 다시 돌려준다.
            total += -heapq.heappop(max_heap)

    print(total)


if __name__ == "__main__":
    main()


# 이진탐색도 시간초과다.
# from bisect import bisect_left


# def main() -> None:
#     # 보석 개수, 가방 개수
#     N, K = map(int, input().split())
#     # 각 보석 무게, 각 보석 가격, 각 보석 무게당 값어치
#     juwels = [(w, p) for _ in range(N) for w, p in [map(int, input().split())]]
#     # 각 가방에 담을 수 있는 최대 무게
#     bags = [int(input()) for _ in range(K)]

#     juwels.sort(key=lambda x: x[1], reverse=True)
#     bags.sort()

#     result = [0] * K

#     for w, p in juwels:

#         i = bisect_left(bags, w)

#         # 인덱스 초과 시 넣을 수 있는 가방이 없다.
#         if i >= K:
#             continue
#         # 이미 사용한 가방이라면 다음으로 큰 가방으로 간다.
#         while i < K - 1 and result[i]:
#             i += 1
#         # 마지막 가방이 사용되었다면 넣을 수 없다.
#         if result[i]:
#             continue
#         # 넣을 수 있는 가장 작은 가방에 넣는다.
#         result[i] = p

#     print(sum(result))


# if __name__ == "__main__":
#     main()
