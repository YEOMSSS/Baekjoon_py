import sys

input = sys.stdin.readline

from math import sqrt


def dist_point_segment(A, B, P):

    # 벡터 계산
    AB = [B[i] - A[i] for i in range(3)]
    AP = [P[i] - A[i] for i in range(3)]

    # AP를 AB로 내적하면 AB방향으로 본 AP의 길이 (정사영)
    dot_AP_AB = sum(AP[i] * AB[i] for i in range(3))
    # AB를 AB로 내적하면 AB길이의 제곱
    dot_AB_AB = sum(AB[i] * AB[i] for i in range(3))

    # AP정사영길이 / AB길이
    t = dot_AP_AB / dot_AB_AB

    # 정사영이 0이 안되면 A 바깥에 P가 존재
    if t < 0:
        # A와의 거리
        return sqrt(sum((P[i] - A[i]) ** 2 for i in range(3)))
    # 정사영이 1을 넘으면 B 바깥에 P가 존재
    elif t > 1:
        # B와의 거리
        return sqrt(sum((P[i] - B[i]) ** 2 for i in range(3)))
    # 0~1 사이에 t가 있으면 수선의 발을 내릴 수 있다.
    else:
        # P에서 벡터AB위에 내린 수선의 발
        closest = [A[i] + t * AB[i] for i in range(3)]
        # 수선의 길이 구하기
        return sqrt(sum((P[i] - closest[i]) ** 2 for i in range(3)))


# 두 3차원 점 사이의 거리 구하기
def dist(X, Y):
    return sqrt(sum((X[i] - Y[i]) ** 2 for i in range(3)))


# 구 방정식과 직선으로 확장한 선분 방정식의 교점 확인
# X(t) = A + Dt  (D = B − A)
# (X − P)² = r²
def intersects_sphere_segment(A, B, P, r):
    D = [B[i] - A[i] for i in range(3)]
    AP = [A[i] - P[i] for i in range(3)]

    # (A + Dt − P)² = r²
    # D²t² + 2 D(A-P) t + (A-P)² - r² = 0
    a = sum(D[i] * D[i] for i in range(3))
    b = 2 * sum(D[i] * AP[i] for i in range(3))
    c = sum(AP[i] * AP[i] for i in range(3)) - r * r

    # 판별식이 0 미만이면 직선에도 닿지 못한다.
    disc = b * b - 4 * a * c
    if disc < 0:
        return False

    sqrt_disc = disc**0.5
    t1 = (-b - sqrt_disc) / (2 * a)
    t2 = (-b + sqrt_disc) / (2 * a)

    # 교점이 선분 내에 하나라도 존재하면 된다.
    return (0 <= t1 <= 1) or (0 <= t2 <= 1)


def b_search(A, B, P):

    left = 0.0
    right = max(dist(P, A), dist(P, B))

    result = 0
    while right - left > 1e-6:
        mid = (left + right) / 2

        # mid를 반지름으로 하는 원이 선분AB와
        # 교점이 생기면 줄여봐도 된다.
        if intersects_sphere_segment(A, B, P, mid):
            right = mid
            result = mid
        # 교점이 없으면 늘려야만 한다.
        else:
            left = mid

    return result


def main() -> None:

    data = list(map(int, input().split()))
    A, B, C = data[:3], data[3:6], data[6:]
    if A == B:
        print(dist(A, C))
        return
    # answer = dist_point_segment(A, B, C)
    answer = b_search(A, B, C)
    print(f"{answer:.6f}")


if __name__ == "__main__":
    main()
