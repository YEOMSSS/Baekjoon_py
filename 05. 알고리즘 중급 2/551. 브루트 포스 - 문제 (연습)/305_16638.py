# Authored by : marigold2003
# Date : 2026-02-09
# Link : https://www.acmicpc.net/problem/16638


import sys

input = sys.stdin.readline


# [Summary] 괄호 추가하기 2

# +, -, *으로 이루어진 수식이 주어진다. 연산자 우선순위는 *가 가장 높으며, +-는 같다.
# 괄호 안에는 연산자가 하나만 들어갈 수 있고, 괄호를 중첩할 수 없다.
# 주어진 수식에 괄호를 적절히 추가해 만들 수 있는 최댓값을 구해보자.
# 수식의 길이는 최대 19. 숫자 10개 연산자 9개다.


def main():

    # [Ideas]

    # 괄호를 추가하는 모든 경우를 다뤄도 시간초과가 크게 나지 않을 것 같다.

    # 1 2 3 4 5

    # 그냥 다 풀어놓고 1234중에 0~2(4//2)개 선택하게 한다.
    # 그리고 선택된것과 그 다음걸 묶으면 된다.
    # 만약 연속된 수가 나온다면 그 조합은 자르면 됨.

    # 수식 계산은 *우선으로 해야하니까
    # 스택으로 대충 풀자.

    ##########

    from itertools import combinations

    N = int(input())
    # 수식을 입력받을 때 숫자는 int형으로 변환해서 리스트로 저장
    expression = [int(x) if x.isdigit() else x for x in input().rstrip()]

    # 들어온 수식을 * 우선으로 연산하는 함수
    def calc(exp) -> int:

        # *연산만 처리해서 새 수식 만들기
        stack = [exp[0]]
        for e in exp[1:]:
            if stack[-1] == "*":
                stack.pop()
                stack.append(stack.pop() * e)
                continue
            stack.append(e)
        res = stack[0]

        for i in range(1, len(stack), 2):
            op = stack[i]  # 연산자
            next_val = stack[i + 1]  # 다음 숫자

            if op == "+":
                res += next_val
            elif op == "-":
                res -= next_val

        return res

    # 결과는 음수가 될 수 있다.
    answer = -sys.maxsize

    # 괄호 시작점을 숫자의 절반보다 많이 선택하는 것은 불가능하다.
    for n in range((N + 1) // 4 + 1):

        # 숫자가 있는 인덱스만 가지고 조합을 뽑아낼 것이다.
        # 마지막 숫자는 뒤에거랑 묶을 수가 없다.
        for comb in combinations(range(0, N - 1, 2), n):

            # 괄호 연속시 배제
            if not all(comb[i] + 2 < comb[i + 1] for i in range(n - 1)):
                continue

            # 수식 계산
            stack = []
            i = 0
            while i < N:
                # i에서 괄호가 시작되면 괄호 연산을 해서 stack에 push
                if i in comb:
                    stack.append(calc(expression[i : i + 3]))
                    i += 3
                    continue

                # 괄호 안에 들어가지 않는 숫자와 부호는 그대로 push
                stack.append(expression[i])
                i += 1

            # 괄호를 전부 처리한 수식을 *우선으로 연산
            answer = max(answer, calc(stack))

    print(answer)

    ##########

    return


# [Review]

# 16637번에서 연산자 우선순위만 추가된 문제이다.
# 수식 계산 방식만 조금 수정하면 된다.


if __name__ == "__main__":
    main()
