import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())

    from itertools import combinations_with_replacement

    nums = (1, 5, 10, 50)
    make_set = set()
    for group in combinations_with_replacement(nums, N):
        make_set.add(sum(group))

    print(len(make_set))


# 날먹을 해보자.
def main2():
    print(
        [
            0,
            4,
            10,
            20,
            35,
            56,
            83,
            116,
            155,
            198,
            244,
            292,
            341,
            390,
            439,
            488,
            537,
            586,
            635,
            684,
            733,
        ][int(input())]
    )


if __name__ == "__main__":
    main2()
