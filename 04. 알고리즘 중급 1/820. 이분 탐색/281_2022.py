# dist가 좁아질수록 c가 커지고, dist가 멀어질수록 c가 작아진다.
# x, y, dist를 이용해서 c를 구하는 공식을 써보자. 렌즈공식
# c = (x높이*y높이)/(x높이+y높이)

# 그냥 수학문제임 수학문제
# 밑변이 같은 뒤집혀 겹친 두 직각삼각형의 빗변의 교점의 높이는
# 두 직각삼각형의 높이에 대해 저 공식을 박으면 됨
# 교점높이역수 = x높이역수 + y높이역수

# 거리가 0으로 갈수록 c는 x,y중 작은값으로 수렴
# 거리가 x,y중 작은값으로 커질수록 c는 0으로 수렴


def b_search(x, y, c):
    left = 0
    right = min(x, y)

    # 첫 result를 0으로 설정했으니, result를 조금씩 키워나갈 것이다.
    result = 0

    # 0.001오차까지 좁힌다.
    while right - left >= 0.001:
        mid = (left + right) / 2

        x_h = (x**2 - mid**2) ** 0.5
        y_h = (y**2 - mid**2) ** 0.5
        temp_c = (x_h * y_h) / (x_h + y_h)

        # 목표보다 클 때, 거리를 늘려본다.
        if temp_c >= c:
            left = mid
            # mid가 커질 일이 없는 경우 result는 갱신되지 않고 0이 나온다.
            # result를 키워야 하니 거리를 늘릴 때 result를 갱신한다.
            result = mid
        # 목표보다 작을 때, 거리를 줄여본다.
        else:
            right = mid
    return result


def main() -> None:
    x, y, c = map(float, input().split())
    print(f"{b_search(x, y, c)}")


if __name__ == "__main__":
    main()
