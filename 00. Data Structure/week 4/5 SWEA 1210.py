import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-03-25
# Problem Number : 1210


# [Summary] 1210. [S/W 문제해결 기본] 2일차 - Ladder1

# 100*100 board 가 0과 1로 채워져 있다.
# 1이 사다리다. 사다리타기 게임을 진행하시오.
# 10개의 테스트케이스가 진행된다.


def main() -> None:

    # [Ideas]

    # 사다리가 문제없는 사다리라고 가정하고 그냥 풀어보자.
    # 목적지에서부터 위로 올라가는 방식으로 풀면 편할듯.

    ##########

    for _ in range(10):
        tc = int(input())

        ladder = [list(map(int, input().split())) for _ in range(100)]

        # 99행에서 시작점인 2를 찾는다.
        startX = 0
        for x in range(100):
            if ladder[99][x] == 2:
                startX = x
                break

        y = 99
        x = startX

        # y가 0에 도달하면 종료
        while y > 0:

            # 0열이 아닌 경우 왼쪽 길 확인
            if x > 0 and ladder[y][x - 1] == 1:
                # 길이 있는 동안 계속 왼쪽으로 이동
                while x > 0 and ladder[y][x - 1] == 1:
                    x -= 1
                y -= 1

            # 99열이 아닌 경우 오른쪽 길 확인
            elif x < 99 and ladder[y][x + 1] == 1:
                # 길이 있는 동안 계속 오른쪽으로 이동
                while x < 99 and ladder[y][x + 1] == 1:
                    x += 1
                y -= 1
            # 길이 없으면 한칸 위로
            else:
                # y -= 1이 반복되고 있다. if에서 빼내고 싶어진다.
                y -= 1

        print(f"#{tc} {x}")

    ##########

    return


# [Review]

# 뭐야, 제약조건 잘 나와있었네.
# 또 내가 문제를 안 읽었구나.

if __name__ == "__main__":
    main()
