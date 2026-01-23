import sys

input = sys.stdin.readline


# 이 문제는 리스트에서 이걸 최댓값으로 만들 수 있는지 확인해야 한다.
# 근데 불가능하다고 해서 이걸 올려야 할지, 내려야 할지 판단이 되나?
# 이게 정말 이분탐색으로 TTTFFFFF형이 나오는 문제인가?

# mid 이상의 값으로 이 리스트를 몇개로 쪼갤 수 있는지 검사하면 되겠다.
# M개 이상으로 쪼갤 수 있으면 숫자를 줄여봐도 될듯. 이게 아닌데?

# mid 이하의 값으로 이 리스트를 몇개로 쪼갤 수 있는지 검사하자.
# M개 이하로 쪼갤 수 있으면 숫자를 줄여봐도 될듯.

# mid가 줄어들수록 잘게 잘라야 한다.
# M개 이하로만 자르면 되니까 한 구역이 최대한 커지게 만들자. 적게자르기 위해

# 1 5 4 6 2 1 3 7,      6
# 1 5 4 6 2 1 3, 7,     5
# 1 5 4, 6 2, 1 3, 7,   4


def check(arr, mid, M):

    count = 1
    curr_min = arr[0]
    curr_max = arr[0]

    for val in arr[1:]:
        curr_min = min(curr_min, val)
        curr_max = max(curr_max, val)

        # 현재 구간의 점수가 mid를 초과하면 구간을 나누고 현재부터 다시 시작
        if curr_max - curr_min > mid:
            count += 1
            curr_min = val
            curr_max = val

    # 나뉜 구간의 수가 M개 이하이면 가능
    return count <= M


def b_search(arr: list, M: int) -> int:
    left = 0
    right = max(arr) - min(arr)

    # 최솟값을 찾는 문제니, 줄여가면서 찾자.
    result = right

    while left <= right:
        mid = (left + right) // 2

        # 나뉜 배열의 점수가 mid 이하로 나오게 해서
        # M 이하로 자를 수 있으면, 더 줄여본다.
        if check(arr, mid, M):
            right = mid - 1
            result = mid
        # M 이상으로 잘라야 한다면, 늘려야만 한다.
        else:
            left = mid + 1

    return result


def solve() -> None:
    # N개원소 배열을 M개이하로 나눈다.
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(b_search(arr, M))


if __name__ == "__main__":
    solve()
