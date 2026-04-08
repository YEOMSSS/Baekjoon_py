import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-04-08
# Problem Number : 1225


# [Summary] 1225. [S/W 문제해결 기본] 7일차 - 암호생성기

# 8개의 숫자가 입력된다.
# 첫번째 숫자를 1 감소시켜 맨 뒤로 보낸다.
# 2, 3, 4, 5 감소시켜 맨 뒤로 보내기를 반복한다. 이를 한 사이클.
# 숫자가 0 밑으로 작아지는 순간이 오면, 0으로 하고 프로그램을 종료한다.


def main() -> None:

    # [Ideas]

    # deque를 쓰기 좋아보이는 문제.
    # rotate를 써볼까?

    ##########

    from collections import deque

    T = 10
    for tc in range(1, T + 1):
        N = int(input())
        dq = deque(map(int, input().split()))

        flag = False
        while True:
            for i in range(1, 6):
                dq[0] -= i
                if dq[0] <= 0:
                    dq[0] = 0
                    flag = True
                dq.rotate(-1)
                if flag:
                    break
            if flag:
                break

        print(f"#{N} {' '.join(map(str, dq))}")

    ##########

    return


# [Review]

# 문제가 오류가 있네. 제일 중요한 걸 틀리게 써두면 어쩌자는거야?
# 0보다 작으면이 아니라 작거나 같으면이잖아?


if __name__ == "__main__":
    main()
