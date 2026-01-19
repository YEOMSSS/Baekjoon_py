import sys

input = sys.stdin.readline


# 분할정복 연습을 해보자. 떠올리기 힘든 아이디어.
# 스카이라인 문제는 웰노운일까?


# sys.setrecursionlimit(200000)


def main() -> None:

    N = int(input())
    buildings = [list(map(int, input().split())) for _ in range(N)]
    # buildings.sort()

    # 머지소트와 비슷하게 반씩 잘라 분할정복한다.
    def solve_R(start, end):

        if end - start == 1:
            l, h, r = buildings[start]
            # 건물 하나의 스카이라인 리스트
            return [[l, h], [r, 0]]

        mid = (start + end) // 2

        # 빌딩들을 반으로 나눠서 스카이라인을 그리고 다시 합친다.
        left_skyline = solve_R(start, mid)
        right_skyline = solve_R(mid, end)

        # merge(left, right) 스카이라인 합치기
        pl, pr = 0, 0
        hl, hr = 0, 0
        merged = []

        left_len, right_len = len(left_skyline), len(right_skyline)
        # 변화점들을 전부 훑는다.
        while pl < left_len and pr < right_len:
            lx, lh = left_skyline[pl]
            rx, rh = right_skyline[pr]

            # 좌스카이라인 변화점 x좌표가 더 작을 때 좌를 다음 변화로 이동
            if lx < rx:
                current_x = lx
                hl = lh
                pl += 1
            # 우스카이라인 변화점 x좌표가 더 작을 때 우를 다음 변화로 이동
            elif lx > rx:
                current_x = rx
                hr = rh
                pr += 1
            # 좌우스카이라인 변화점 x좌표가 동일할 때는 둘 다 다음 변화로 이동
            else:  # lx == rx
                current_x = lx
                hl, hr = lh, rh
                pl += 1
                pr += 1

            # 좌우높이 중 더 높은 값이 현재 스카이라인의 높이가 된다.
            current_max_h = max(hl, hr)

            # 현재 스카이라인 높이가 이전 변화와 동일할 경우 스킵
            if merged and merged[-1][1] == current_max_h:
                continue
            merged.append([current_x, current_max_h])

        if pl < left_len:
            # 나머지 붙일 때도 높이 중복 확인
            if merged and merged[-1][1] == left_skyline[pl][1]:
                merged.extend(left_skyline[pl + 1 :])
            else:
                merged.extend(left_skyline[pl:])

        if pr < right_len:
            # 나머지 붙일 때도 높이 중복 확인
            if merged and merged[-1][1] == right_skyline[pr][1]:
                merged.extend(right_skyline[pr + 1 :])
            else:
                merged.extend(right_skyline[pr:])

        return merged

    for x, h in solve_R(0, N):
        print(x, h, end=" ")


if __name__ == "__main__":
    main()
