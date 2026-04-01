import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-04-01
# Problem Number : 4874


# [Summary] 4874. [S/W 문제해결 기본] 5일차 - Forth

# 입력된 후위표기식의 계산 결과를 출력하시오.
# 오류일 경우 error를 출력한다.


def main() -> None:

    # [Ideas]

    # 배운 그대로 가져오면 된다.
    # 에러 처리만 해주자.

    ##########

    T = int(input())

    for tc in range(1, T + 1):
        # 후위표기식을 계산해보자.
        postfix = list(input().split())
        stack = []

        Flag = True
        for term in postfix:
            if term == ".":
                break

            if term.isdigit():
                stack.append(int(term))

            else:
                if len(stack) < 2:
                    Flag = False
                    break

                right = stack.pop()
                left = stack.pop()

                if term == "+":
                    stack.append(left + right)
                elif term == "-":
                    stack.append(left - right)
                elif term == "*":
                    stack.append(left * right)
                elif term == "/":
                    stack.append(left // right)

        if Flag and len(stack) == 1:
            print(f"#{tc} {stack[-1]}")
        else:
            print(f"#{tc} error")

    ##########

    return


# [Review]

# 어느 타이밍에 에러가 날지 생각해보자.
# 정수나눗셈을 사용할 것.


if __name__ == "__main__":
    main()
