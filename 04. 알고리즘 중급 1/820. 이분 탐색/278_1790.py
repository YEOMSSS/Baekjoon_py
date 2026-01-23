import sys

input = sys.stdin.readline


# 1 ~ 9                     9개
# 10 ~ 99                   90*2개
# 100 ~ 999                 900*3개
# ...                       ...
# 10_000_000 ~ 99_999_999   90_000_000*8개

# 일단 K가 어떤 범위에 속하는지 확인한다.

# 이걸 이분탐색으로 어떻게 풀지? 에...
# https://kyu9341.github.io/algorithm/2020/03/03/algorithm1790/
# N까지의 자릿수를 구하는 함수를 만들어 이분탐색으로 1~100_000_000 탐색시마다 함수를 돌려 찾는다.

# 너무 내장함수를 사용하려고 하지 말자. tony9402에서 했던 걸 떠올려라.
# 이분탐색의 사용처는 값의 비교에만 있는 것이 아니니까.


def main() -> None:

    # 1~N 숫자묶음, 목표 자리
    N, K = map(int, input().split())

    # i번째 묶음에서의 목표 자리
    Ki = K

    # 1~99_999_999까지 붙이면 8_888_888_889자리
    len_to_K = 0
    for i in range(9):
        curr = 10**i * 9 * (i + 1)

        len_to_K += curr
        if len_to_K >= K:
            break

        Ki -= curr

    # 여기서 i자리수를 묶어놓은 묶음에 K번째가 포함된다.

    # 올림법칙을 이용
    target_num = 10**i + ((Ki + (i + 1) - 1) // (i + 1) - 1)

    if target_num > N:
        print(-1)
        return

    # 나머지가 1일때 맨앞에거, 나머지가 2일때 그다음거, ... , 나머지가 0일때 맨끝에거
    print(str(target_num)[Ki % (i + 1) - 1])


if __name__ == "__main__":
    main()
