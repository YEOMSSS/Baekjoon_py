import sys

input = sys.stdin.readline

from itertools import permutations
from bisect import bisect_right


def main() -> None:
    A, B = input().split()

    # permutations는 문자열도 잘 다룬다.
    # permutations에서 r을 생략하면 len(list)가 기본값으로 들어간다.
    perms = set(int("".join(p)) for p in permutations(A) if p[0] != "0")
    candidates = sorted(list(perms))
    # candidates = sorted(list(set(int("".join(p)) for p in permutations(A))))

    # B보다 큰 수의 시작 -1 = B보다 작거나 같은 것들 중 최댓값
    index = bisect_right(candidates, int(B)) - 1

    print(candidates[index] if index >= 0 else -1)


if __name__ == "__main__":
    main()
