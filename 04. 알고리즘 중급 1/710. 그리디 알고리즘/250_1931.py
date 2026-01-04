import sys

input = sys.stdin.readline


# 끝나는 시간이 가장 빠른 회의를 선택한다.
# 다음으로 회의가 빨리 끝나는 회의 중 겹치지 않는 회의를 선택한다.
def main():

    N = int(input())
    meetings = []

    for _ in range(N):
        start, end = map(int, input().split())
        meetings.append((end, start))  # 끝나는 시간 기준

    meetings.sort()

    last_end = 0
    count = 0

    # 끝나는 시간순으로 정렬되어 들어온다.
    for end, start in meetings:
        # 시작시각이 이전 종료시각 이전이 아닌 경우 카운트한다.
        if start >= last_end:
            # 종료시각을 갱신한다.
            last_end = end
            count += 1

    print(count)


if __name__ == "__main__":
    main()


# 그리디를 안쓰면 너무 고달프다. 고달파...
"""
import sys

input = sys.stdin.readline

# 정렬하고 작은거부터 더하는 행위를 10만번 해야하는가?
# 시작시간이 같은애들은 작은애들로 다 합쳐도 된다.

from bisect import bisect_right


def main() -> None:
    N = int(input())

    meetings = {}

    same_counter = {}
    for _ in range(N):
        start, end = map(int, input().split())
        if start == end:
            same_counter[start] = same_counter.get(start, 0) + 1
            continue

        meetings[start] = min(meetings.get(start, float("inf")), end)

    keys_sorted = sorted(meetings.keys())

    # 회의가 끝나는 시각 저장
    last = meetings[keys_sorted[-1]]

    result = 0
    for k in keys_sorted:
        count = 0
        current = k

        while current <= last:
            count += same_counter.get(current, 0) + 1

            next_time = meetings[current]

            idx = bisect_right(keys_sorted, next_time)
            if idx == len(keys_sorted):
                break
            current = keys_sorted[idx]

        result = max(result, count)

    print(result)


if __name__ == "__main__":
    main()
"""
