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
# Problem Number : 1224


# [Summary] 1224. [S/W 문제해결 기본] 6일차 - 계산기3

# (, ), +, *, 숫자로만 이뤄진 수식이 입력된다.
# 후위표기식으로 변환한 후, 수식의 결과를 출력하시오.


def main() -> None:

    # [Ideas]

    #

    ##########

    # 민증 까기
    def precedendce(op):
        if op in ("*", "/"):
            return 2
        elif op in ("+", "-"):
            return 1
        elif op in ("("):
            return 0

        return -1

    for tc in range(1, 11):
        N = int(input())
        Data = input().rstrip()

        stack = []
        output = []

        for term in Data:

            if term.isdigit():
                output.append(int(term))

            elif term == "(":
                stack.append(term)

            elif term == ")":
                # 열린괄호 나올때까지 pop해서 output에 append
                while stack:
                    op = stack.pop()

                    if op == "(":
                        break
                    else:
                        output.append(op)

            elif term in "+*":

                while stack:
                    # 일단 pop하기 전에 뭐가 있는지 보자.
                    op = stack[-1]

                    # 형님이 동생 밑에 있긴 짜증나서 나온다.
                    if precedendce(term) <= precedendce(op):
                        output.append(stack.pop())

                    # 형님이 내 위로 오면 이해해야지.
                    else:
                        break

                # 스택에 아무것도 없어도 들어간다.
                stack.append(term)

        # 스택에 남은거 다 털자.
        while stack:
            output.append(stack.pop())

        ##################################################

        # 후위표기식을 계산해보자.

        for term in output:
            if type(term) is int:
                stack.append(term)

            else:
                right = stack.pop()
                left = stack.pop()

                if term == "+":
                    stack.append(left + right)
                elif term == "*":
                    stack.append(left * right)

        print(f"#{tc} {stack[-1]}")

    ##########

    return


# [Review]

# 이건 배운 내용에서 고칠 게 하나도 없다.


if __name__ == "__main__":
    main()
