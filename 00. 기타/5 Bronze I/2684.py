import sys
input = sys.stdin.readline

def main():
    N = int(input())

    for _ in range(N):
        coins = list(input())

        answer = [0] * 8
        for i in range(38):
            match coins[i : i + 3]:
                case ["T", "T", "T"]:
                    answer[0] += 1
                case ["T", "T", "H"]:
                    answer[1] += 1
                case ["T", "H", "T"]:
                    answer[2] += 1
                case ["T", "H", "H"]:
                    answer[3] += 1
                case ["H", "T", "T"]:
                    answer[4] += 1
                case ["H", "T", "H"]:
                    answer[5] += 1
                case ["H", "H", "T"]:
                    answer[6] += 1
                case ["H", "H", "H"]:
                    answer[7] += 1

        print(*answer)

if __name__ == "__main__":
    main()