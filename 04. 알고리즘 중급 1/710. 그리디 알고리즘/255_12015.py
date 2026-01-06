import sys

input = sys.stdin.readline

# LIS(가장 긴 증가하는 부분 수열) 문제는 dp아니면 이분탐색으로 해결한다.
# 범위가 작으면 dp로도 가볍게 풀 수 있지만, 입력이 커지면 이분탐색을 사용해야 한다.

# 길이만 구하면 되니까 내용물을 유지할 필요는 없을듯.

# 동일한 원소를 찾을 때 인덱스를 덮어야 하니까 left로 찾는다.
# 57 97 57 97이 들어올 때 LIS가 57 57 97이 되는 불상사가 있을 수 있다.

from bisect import bisect_left


def main() -> None:
    N = int(input())
    nums = list(map(int, input().split()))

    LIS = [0]

    for n in nums:

        # 수가 현재까지 나온 수 중 제일 크면 append
        if n > LIS[-1]:
            LIS.append(n)
            continue

        # LIS[-1]보다 수가 작으면 자신보다 큰 가장 가까운 수에 덧씌운다.
        # LIS는 정렬되어 있으므로, 수가 들어갈 인덱스를 이분탐색으로 찾을 수 있다.
        idx = bisect_left(LIS, n)
        LIS[idx] = n

    # LIS는 갱신이 되다 말다 하게 되는데, 상관없다.
    # 어차피 최대 길이만 구하면 되니까.

    # 처음에 기본으로 넣어뒀던 0만 빼주면 된다.
    print(len(LIS) - 1)


if __name__ == "__main__":
    main()
