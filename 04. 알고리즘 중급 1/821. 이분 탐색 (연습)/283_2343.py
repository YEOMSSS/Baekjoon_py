import sys

input = sys.stdin.readline


# 이분탐색으로 블루레이의 길이를 찾는다. M은 사용가능한 블루레이의 개수
def b_search(lectures: list, M: int) -> int:

    left = max(lectures)
    right = sum(lectures)

    result = 0

    while left <= right:
        mid = (left + right) // 2

        count = 0
        temp = 0
        for lec in lectures:
            if temp + lec <= mid:
                temp += lec
            else:
                temp = lec
                count += 1
        if temp:
            count += 1

        # 블루레이의 개수가 M보다 작거나 같으면 블루레이의 길이를 줄여봐도 된다.
        if count <= M:
            right = mid - 1
            result = mid
        # 블루레이의 개수가 M보다 크면 블루레이의 길이를 늘려야만 한다.
        else:
            left = mid + 1

    return result


def main() -> None:
    N, M = map(int, input().split())
    lectures = list(map(int, input().split()))

    print(b_search(lectures, M))


if __name__ == "__main__":
    main()
