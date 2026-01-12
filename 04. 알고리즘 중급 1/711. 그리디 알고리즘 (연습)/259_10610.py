import sys

input = sys.stdin.readline


# 30의 배수라.
# 3의 배수는 모든 자리를 합했을 때 그게 3이 되면 된다.
# 30의 배수는 그 수의 마지막 자리가 0이면 되겠지.
# 마지막 자리가 0이 되게 하여 높은 수부터 순서대로 쓰면 된다. 자동으로 마지막은 0.


def main() -> None:
    Ns = list(map(int, input().rstrip()))

    # 0이 포함되지 않은 수면 30의 배수를 만들 수 없다.
    if 0 not in Ns:
        print(-1)
        return

    # 수가 3의 배수가 아니면 30의 배수를 만들 수 없다.
    if sum(Ns) % 3:
        print(-1)
        return

    print("".join(map(str, sorted(Ns, reverse=True))))


if __name__ == "__main__":
    main()
