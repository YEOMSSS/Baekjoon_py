import sys

input = sys.stdin.readline


# 1 2 0 4 0 0 0 8 9

# 1 ~ 최대좌표 // 공유기의 개수. 이걸 이분탐색으로 계속 판정하면 되겠네?


def b_search(house_coords: list, target: int) -> int:

    left = 0
    # 공유기의 개수 - 1 로 나눠줘야 최대 간격이 나온다.
    right = house_coords[-1] // (target - 1)

    result = 0

    while left <= right:
        mid = (left + right) // 2

        count = 1
        prev = house_coords[0]
        for coord in house_coords[1:]:
            # 설치 간격 바깥에 집이 있으면 설치
            if coord - prev > mid:
                count += 1
                prev = coord
            # 설치 간격 안에 집이 있으면 설치 불가

        # 현재 간격으로 설치한 공유기 카운트가 목표보다 크면 설치 가능
        # 현재 간격으로 설치가 가능하다면 늘려봐도 된다.
        if count >= target:
            result = mid
            left = mid + 1
        # 현재 간격으로 설치가 불가하다면 줄여야만 한다.
        else:
            right = mid - 1

    return result


def main() -> None:
    N, C = map(int, input().split())
    house_coords = list(int(input()) for _ in range(N))
    house_coords.sort()

    print(b_search(house_coords, C) + 1)


if __name__ == "__main__":
    main()
