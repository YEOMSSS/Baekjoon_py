# 02.203.112_1935 후위표기식 2 와 거의 같은 문제이다.

import sys
input = sys.stdin.readline

string = list(input().strip())

stack = []

for char in string:
    if char in "+-*/":
        b = stack.pop()
        a = stack.pop()

        match char:
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "*":
                stack.append(a * b)
            case "/":
                stack.append(a // b) # 정수 나눗셈.
    else:
        stack.append(int(char))

print(stack[0])

# 수식의 계산 중간 과정의 모든 결과는 항상 """정수"""이고
# 아!!!! a // b 였다.