import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

###########


# greedy 냄새가 나는데.
# 역순으로 읽으면서 더 큰게 나올때까지 계속 팔면 된다.
def main():
    T = int(input())

    for tc in range(1, T + 1):
        howmany = int(input())  # <= 1M
        Data = list(map(int, input().split()))

        sofarMax = 0
        profit = 0

        for i in range(howmany - 1, -1, -1):
            curr = Data[i]
            if curr <= sofarMax:
                profit += sofarMax - curr
            # 동일 시 갱신하지 않는 편이 효율적
            else:
                sofarMax = curr

        print(f"#{tc} {profit}")


if __name__ == "__main__":
    main()
