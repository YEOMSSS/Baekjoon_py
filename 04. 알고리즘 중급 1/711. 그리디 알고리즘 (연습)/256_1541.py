# 무조건 더하기 우선으로 다 더해버리면 된다.
# 그리고 나서 빼기만 남은 식을 처리하면 끝.


# 파이썬에는 split이 있으니까.
def main2() -> None:
    expression = input().split("-")

    result = sum(map(int, expression[0].split("+")))

    for e in expression[1:]:
        minus = sum(map(int, e.split("+")))
        result -= minus

    print(result)


def main() -> None:
    string = input().rstrip()

    start = 0
    end = 0

    expression = []
    for i, ch in enumerate(string):
        if ch == "+" or ch == "-":
            expression.append(int(string[start:end]))
            expression.append(ch)
            start = i + 1
            end = i + 1
        else:
            end += 1

    expression.append(int(string[start:end]))

    stack = []
    for e in expression:
        if e == "-":
            continue

        if stack and stack[-1] == "+":
            stack.pop()
            temp = stack.pop()
            stack.append(temp + e)

        else:
            stack.append(e)

    result = stack[0]
    for n in stack[1:]:
        result -= n

    print(result)


if __name__ == "__main__":
    main2()
