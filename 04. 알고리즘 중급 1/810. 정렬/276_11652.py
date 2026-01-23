import sys

input = sys.stdin.readline

from collections import Counter


def main() -> None:

    N = int(input())
    arr = [int(input()) for _ in range(N)]

    # 카운터로 숫자 빈도 세기
    arr_Counter = Counter(arr)

    # most_common으로 최빈값 가져오기
    count_max = arr_Counter.most_common(1)[0][1]

    # 최빈값을 value로 가지는 key중 가장 작은 key값 출력
    answer = min(key for key, value in arr_Counter.items() if value == count_max)
    print(answer)


if __name__ == "__main__":
    main()
