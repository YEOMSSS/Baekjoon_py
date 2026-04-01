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
# Problem Number : 4866


# [Summary] 4866. [S/W 문제해결 기본] 4일차 - 괄호검사

# 괄호가 포함된 문자열이 입력된다.
# ()와 {}가 올바르게 짝지어진 문자열인지 검사하시오.


def main() -> None:

    # [Ideas]

    # 배운 대로 하면 된다.
    # 다만, 괄호만 있는 문자열이 아니기 때문에
    # 괄호가 아닌 것이 입력되었을 때는 pass해줘야 한다.

    ##########

    T = int(input())
    for tc in range(1, T + 1):

        Data = input().rstrip()
        answer = 1

        stack = []
        for ch in Data:
            if ch in "({":
                stack.append(ch)

            elif ch in ")}":
                # 스택이 비었는데 닫힌괄호면 비정상
                if not stack:
                    answer = 0
                    break

                elif (ch == ")" and stack[-1] == "(") or (
                    ch == "}" and stack[-1] == "{"
                ):
                    stack.pop()

                else:
                    answer = 0
                    break

            # 괄호가 아니면 pass. 없어도 되는 코드다.
            else:
                pass

        if stack:
            answer = 0

        print(f"#{tc} {answer}")

    ##########

    return


# [Review]

# 배운 거에서 조금 더.


if __name__ == "__main__":
    main()
