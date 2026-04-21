# 민증 까기
def precedendce(op):
    if op in ("*", "/"):
        return 2
    elif op in ("+", "-"):
        return 1
    elif op in ("("):
        return 0

    return -1


Data = "1+2*3*(4+5)/6"

stack = []
output = []

for term in Data:

    if term.isdigit():  # 정수 string임?
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

    elif term in "+-*/":

        while stack:
            # 일단 pop하기 전에 뭐가 있는지 보자.
            op = stack[-1]

            # 형님이 동생 밑에 있긴 짜증나서 나온다. 같아도 나온다.
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

print(output)

##################################################

# 후위표기식을 계산해보자.

for term in output:
    if type(term) is int:  # 교수님은 왜 위에서 int로 바꿔놓고 isdigit을 또 쓰고 계시지?
        stack.append(term)

    else:
        right = stack.pop()
        left = stack.pop()

        if term == "+":
            stack.append(left + right)
        elif term == "-":
            stack.append(left - right)
        elif term == "*":
            stack.append(left * right)
        elif term == "/":
            stack.append(left / right)

print(stack)
