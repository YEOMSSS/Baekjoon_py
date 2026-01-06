import sys

input = sys.stdin.readline


# 253_1202번과 비슷한 논리로 풀면 된다.
# 말일부터 세서, n일까지 해야하는 강의는 1~n-1에도 무조건 할 수 있는 것을 이용.
# 힙에 그 날에 가능한 걸 전부 push한다. 그리고 날마다 최대힙을 하나씩 pop해서 꺼내면 된다.
import heapq


def main():
    # 대학의 개수
    N = int(input())
    # 강연료, 기한
    lecture_information = [tuple(map(int, input().split())) for _ in range(N)]

    # 기한 기준 역순으로 정렬
    lecture_information.sort(key=lambda x: x[1], reverse=True)

    max_heap = []
    total = 0

    idx = 0
    # 10000일 ~ 1일 순서로 확인
    for d in range(10000, 0, -1):
        # 현재 일자부터 가능한 강의 최대힙에 push
        while idx < N and lecture_information[idx][1] == d:
            heapq.heappush(max_heap, -lecture_information[idx][0])
            idx += 1

        # 현재 일자에 할 수 있는 가장 비싼 강의 pop
        if max_heap:
            total += -heapq.heappop(max_heap)

    print(total)


if __name__ == "__main__":
    main()
