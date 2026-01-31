# 애들이 20억명이 있다.
# 놀이기구는 1만개가 있다.
# 놀이기구는 1~30분의 이용시간을 갖는다.

# 일단 마지막 애까지 태우는 데 몇분이 걸리는지 보자.

import sys

input = sys.stdin.readline


# N명의 애들을 놀이기구에 태울 수 있는 시간의 최솟값을 찾는다.
def b_search(times, N, M) -> int:

    left = 0
    right = min(times) * N

    # 줄여가면서 찾을 것이다.
    result = right

    while left <= right:
        mid = (left + right) // 2

        # 일단 다 태우고 시작한다.
        count = M
        for t in times:
            # 이 놀이기구에 mid분동안 몇명 태울 수 있는가
            count += mid // t

        # 태울 수 있으면 시간을 줄여봐도 된다.
        if count >= N:
            right = mid - 1
            result = mid
        # 태울 수 없다면 시간을 늘려야만 한다.
        else:
            left = mid + 1

    # N명을 모두 처리할 수 있는 시간의 최솟값 반환
    return result


def main() -> None:
    N, M = map(int, input().split())
    times = tuple(map(int, input().split()))

    # 인원수가 놀이기구 수보다 적은 경우
    if N <= M:
        print(N)
        return

    # N명을 모두 태우는 시간의 최솟값
    N_time = b_search(times, N, M)

    # N_time에 누군가 탔을 것이다.
    # 그렇기에 N_time-1에 놀이기구는 하나 이상 비어 있게 된다.

    count = M
    candidates = []

    for i, t in enumerate(times):
        count += (N_time - 1) // t

        # N_time에 비는 놀이기구(N_time에 입장이 있었던 놀이기구)
        if N_time % t == 0:
            candidates.append(i + 1)

    print(candidates[N - count - 1])


if __name__ == "__main__":
    main()
