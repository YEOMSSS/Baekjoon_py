# Authored by : marigold2003
# Date : 2026-01-29
# Link : https://www.acmicpc.net/problem/16637

import sys

input = sys.stdin.readline


# [Summary]

# +, -, *으로 이루어진 수식이 주어진다. 연산자에 우선순위는 없다.
# 괄호 안에는 연산자가 하나만 들어갈 수 있고, 괄호를 중첩할 수 없다.
# 주어진 수식에 괄호를 적절히 추가해 만들 수 있는 최댓값을 구해보자.
# 수식의 길이는 최대 19. 숫자 10개 연산자 9개다.


def main():

    # [Ideas]

    # 괄호를 추가하는 모든 경우를 다뤄도 시간초과가 크게 나지 않을 것 같다.

    # 1 2 3 4 5

    # 12를 묶고 나머지를 그냥 두거나 묶는다
    # 1을 내버려두고 23을 묶고 나머지를 그냥 두거나 묶는다
    # 1,2 를 내버려두고 34를 묶고 나머지를 그냥 두거나 묶는다
    # 1,2,3 을 내버려두고 45를 묶고 나머지를 그냥 두거나 묶는다
    # 1,2,3,4를 내벼려두면 5도 묶을 수 없다.
    # 이런식으로 브루트포스 돌리면 될거같은데?

    # 아니, 굳이 이렇게 조건을 넣을 필요가 없다.
    # 그냥 다 풀어놓고 1234중에 0~4개 선택하게 한다.
    # 그리고 선택된것과 그 다음걸 묶으면 된다.
    # 만약 연속된 수가 나온다면 그 조합은 자르면 됨.

    # 수식 계산은 대충하자.

    ##########

    from itertools import combinations

    N = int(input())
    # expression = list(input().rstrip())
    # 수식을 입력받을 때 숫자는 int형으로 변환해서 리스트로 저장
    expression = [int(x) if x.isdigit() else x for x in input().rstrip()]

    # 들어온 수식을 우선순위 없이 순서대로 연산하는 함수
    def calc(exp) -> int:

        res = exp[0]

        for i in range(1, len(exp), 2):
            op = exp[i]  # 연산자
            next_val = exp[i + 1]  # 다음 숫자

            if op == "+":
                res += next_val
            elif op == "-":
                res -= next_val
            elif op == "*":
                res *= next_val

        return res

    # 결과는 음수가 될 수 있다.
    answer = -sys.maxsize

    # 괄호 시작점을 숫자의 절반보다 많이 선택하는 것은 불가능하다.
    for n in range((N + 1) // 4 + 1):

        # 숫자가 있는 인덱스만 가지고 조합을 뽑아낼 것이다.
        # 마지막 숫자는 뒤에거랑 묶을 수가 없다.
        for comb in combinations(range(0, N - 1, 2), n):

            # for i in range(n - 1):
            #     if comb[i] + 2 == comb[i + 1]:
            #         continue
            # 괄호 연속시 배제
            if not all(comb[i] + 2 < comb[i + 1] for i in range(n - 1)):
                continue

            # 수식 계산
            stack = []
            i = 0
            while i < N:
                if i in comb:
                    stack.append(calc(expression[i : i + 3]))
                    i += 3
                    continue
                stack.append(expression[i])
                i += 1

            answer = max(answer, calc(stack))

    print(answer)

    ##########

    return


# [Review]

# 지능을 곁들인 브루트포스
# 경우의 수가 생각보다 적다는 것을 깨닫는 것이 중요하다.

if __name__ == "__main__":
    main()


# 그냥 str만으로 풀어낸 경우
"""
# Authored by : marigold2003
# Date : 2026-01-29
# Link : https://www.acmicpc.net/problem/16637

import sys

input = sys.stdin.readline


# [Summary]

# +, -, *으로 이루어진 수식이 주어진다. 연산자에 우선순위는 없다.
# 괄호 안에는 연산자가 하나만 들어갈 수 있고, 괄호를 중첩할 수 없다.
# 주어진 수식에 괄호를 적절히 추가해 만들 수 있는 최댓값을 구해보자.
# 수식의 길이는 최대 19. 숫자 10개 연산자 9개다.


def main():

    # [Ideas]

    # 괄호를 추가하는 모든 경우를 다뤄도 시간초과가 크게 나지 않을 것 같다.

    # 1 2 3 4 5

    # 12를 묶고 나머지를 그냥 두거나 묶는다
    # 1을 내버려두고 23을 묶고 나머지를 그냥 두거나 묶는다
    # 1,2 를 내버려두고 34를 묶고 나머지를 그냥 두거나 묶는다
    # 1,2,3 을 내버려두고 45를 묶고 나머지를 그냥 두거나 묶는다
    # 1,2,3,4를 내벼려두면 5도 묶을 수 없다.
    # 이런식으로 브루트포스 돌리면 될거같은데?

    # 아니, 굳이 이렇게 조건을 넣을 필요가 없다.
    # 그냥 다 풀어놓고 1234중에 0~4개 선택하게 한다.
    # 그리고 선택된것과 그 다음걸 묶으면 된다.
    # 만약 연속된 수가 나온다면 그 조합은 자르면 됨.

    # 수식 계산은 대충하자.

    ##########

    from itertools import combinations

    N = int(input())
    expression = input().rstrip()

    # 들어온 수식을 우선순위 없이 순서대로 연산하는 함수
    def calc(exp) -> int:

        stack = [int(exp[0])]

        for curr in exp[1:]:
            if curr == "+" or curr == "-" or curr == "*":
                stack.append(curr)
                continue

            op = stack.pop()
            match op:
                case "+":
                    stack.append(stack.pop() + int(curr))
                case "-":
                    stack.append(stack.pop() - int(curr))
                case "*":
                    stack.append(stack.pop() * int(curr))

        return stack.pop()

    # 결과는 음수가 될 수 있다.
    answer = -sys.maxsize

    # 괄호 시작점을 숫자의 절반보다 많이 선택하는 것은 불가능하다.
    for n in range((N + 1) // 4 + 1):

        # 숫자가 있는 인덱스만 가지고 조합을 뽑아낼 것이다.
        # 마지막 숫자는 뒤에거랑 묶을 수가 없다.
        for comb in combinations(range(0, N - 1, 2), n):

            # 괄호 연속시 배제
            for i in range(n - 1):
                if comb[i] + 2 == comb[i + 1]:
                    continue

            # 수식 계산
            stack = []
            i = 0
            while i < N:
                if i in comb:
                    stack.append(calc(expression[i : i + 3]))
                    i += 3
                    continue
                stack.append(expression[i])
                i += 1

            answer = max(answer, calc(stack))

    print(answer)

    ##########

    return


# [Review]

# 지능을 곁들인 브루트포스
# 경우의 수가 생각보다 적다는 것을 깨닫는 것이 중요하다.

if __name__ == "__main__":
    main()

"""
