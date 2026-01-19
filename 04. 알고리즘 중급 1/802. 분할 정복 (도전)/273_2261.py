import sys

input = sys.stdin.readline


# 스위핑이란 무엇인가? 평면이나 공간상의 요소를 직선으로 쓸어내리듯 처리하는 기하 알고리즘
# 여기에 분할정복을 끼얹어볼까?

# 우선 점들을 분할정복으로 나누고, 그 안에서 스위핑으로 최솟값을 찾아보자.

# O(N logN)이라서 10만이 들어와도 재귀가 깊어봤자 20이 안 된다.
# 머지소트식 분할정복에는 재귀깊이 설정이 필요 없다.
# sys.setrecursionlimit(200000)


# 두 점 사이의 거리의 제곱 계산, 루트 안씌울거임
def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def main_sweeping() -> None:
    from bisect import bisect_left, insort

    N = int(input())

    points = [tuple(map(int, input().split())) for _ in range(N)]
    # 스위핑을 위한 x좌표 기준 정렬
    points.sort()

    # 중복 점 예외 처리 (동일 좌표가 있으면 최단 거리는 0)
    if len(set(points)) != N:
        print(0)
        return

    # 초기 최솟값은 첫 번째와 두 번째 점의 거리
    dist = dist_sq(points[0], points[1])

    # 슬라이딩 윈도우에 포함되는 점들의 리스트. (y, x)형으로 저장한다. 이분탐색 편하게 하게
    window = [(points[0][1], points[0][0]), (points[1][1], points[1][0])]
    window.sort()

    # x좌표 윈도우의 왼쪽 끝을 가리키는 포인터
    start = 0

    # 세 번째 점부터 스위핑 시작. 슬라이딩 윈도우로 모든 점을 스위핑
    for i in range(2, N):
        curr = points[i]

        # x좌표에 대해 스위핑
        # curr와의 x좌표 차이가 현재 dist보다 크면 윈도우를 이동시켜 영구 삭제
        while start < i:
            target = points[start]
            # 양끝 x좌표 거리가 dist를 넘으면 빼버린다.
            if (curr[0] - target[0]) ** 2 > dist:
                # x좌표 정렬된 i이므로 y좌표 정렬된 윈도우에선 remove를 써야한다.
                window.remove((target[1], target[0]))
                # 윈도우 이동
                start += 1
            else:
                break

        # y좌표에 대해 스위핑
        # 바구니에 남은 점들 중 현재 점의 y값 기준 +dist, -dist 범위 내에 있는 점만 검사
        d = int(dist**0.5)

        # y좌표 범위의 시작과 끝 인덱스를 윈도우 내에서 이진 탐색으로 빠르게 찾음
        # 윈도우 내 x좌표는 전부 dist 이내임이 확인되어있으니 start엔 -inf, end엔 inf를 때려박는다.
        start_y = bisect_left(window, (curr[1] - d, -float("inf")))
        end_y = bisect_left(window, (curr[1] + d, float("inf")))

        # x, y좌표에 대해 스위핑을 모두 마친 점들에 대해서 dist 최솟값 갱신
        for j in range(start_y, end_y):
            # 후보 점과 거리 계산. 윈도우에 yx를 거리계산을 위해 xy로 바꿔쓴다.
            temp = (window[j][1], window[j][0])
            dist = min(dist, dist_sq(curr, temp))

        # 윈도우를 이동시켜 현재 점을 존에 포함시킨다. insort를 이용해 y좌표 정렬을 유지
        insort(window, (curr[1], curr[0]))

    print(dist)


def main_conquer() -> None:
    N = int(input())

    points = [tuple(map(int, input().split())) for _ in range(N)]
    # 분할정복을 위한 x좌표 기준 정렬
    points.sort()

    # 중복 점 예외 처리 (동일 좌표가 있으면 거리는 0)
    if len(set(points)) != N:
        print(0)
        return

    # 분할정복 like MergeSort
    def solve_R(start, end):

        # 점이 3개 이하일 때는 완전탐색. 2 아니면 3이 들어온다.
        if end - start <= 3:
            min_dist = float("inf")

            for i in range(start, end):
                for j in range(i + 1, end):
                    min_dist = min(min_dist, dist_sq(points[i], points[j]))

            return min_dist

        # 가운데 점 인덱스
        mid = (start + end) // 2

        # 좌우 영역이 갈라져 있다 치고, 좌측최솟값과 우측최솟값 중 더 작은 걸 일단 선택
        dist = min(solve_R(start, mid), solve_R(mid, end))

        # 병합할거임. 중앙 점 기준으로 위 dist보다 작은게 있으면 그걸로 갱신한다.

        # 중앙 경계선에서 x좌표 거리가 dist 미만인 점들만 수집
        mid_zone = []

        mid_x = points[mid][0]
        # 처음부터 끝까지 훑어서 mid_x - dist ~ mid_x + dist 사이의 점만 찾는다.
        for i in range(start, end):
            # 거리의 제곱으로 코드를 돌리고 있으니 제곱해준다.
            if (points[i][0] - mid_x) ** 2 < dist:
                mid_zone.append(points[i])

        # 스위핑을 위한 y좌표 기준 오름차순 정렬
        mid_zone.sort(key=lambda x: x[1])

        # y좌표 스위핑. y좌표간 거리가 dist 이내인 점들만 비교
        m = len(mid_zone)

        # y좌표가 작은 점부터 비교의 주체로 설정
        for i in range(m):
            # i보다 y좌표가 큰 점들을, y좌표가 작은 점부터 비교
            for j in range(i + 1, m):

                # mid_zone이 y좌표 기준 오름차순이므로 이번 j가 dist를 넘어가면 다음 j도 dist를 넘길 것이다.
                # y좌표 차이가 dist 이상이면 더 이상 볼 필요 없음
                if (mid_zone[i][1] - mid_zone[j][1]) ** 2 >= dist:
                    break

                # 병합된 점의 집합에서의 최솟값 갱신
                dist = min(dist, dist_sq(mid_zone[i], mid_zone[j]))

        return dist

    # 결과 출력
    print(solve_R(0, N))


if __name__ == "__main__":
    # main_conquer()
    main_sweeping()
