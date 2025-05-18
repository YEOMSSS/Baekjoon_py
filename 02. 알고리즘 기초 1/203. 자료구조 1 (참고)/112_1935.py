'''
문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다.
(여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다)
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.
3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다,
그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.

예제 입력 1 
5
ABC*+DE/-
1
2
3
4
5
예제 출력 1 
6.20
예제 입력 2 
1
AA+A+
1
예제 출력 2 
3.00
'''
# 이제 실버에는 쫄지 않는 사람이 되어버렸다

# 5 1 2 + 4 * + 3 - 후위표기식
# 5 + ((1 + 2) * 4) - 3 중위표기식
# 후위표기식이 뭔지 알았으니 달려 보자.

# 트릭컬 city night와 함께
'''
import sys
input = sys.stdin.readline

cnt = int(input())

string = list(input().strip())

alpha_dict = {}

for ch in range(65, 65 + cnt): # A(65)
    alpha = chr(ch)
    num = int(input())
    alpha_dict[alpha] = num # 딕셔너리는 이런식으로 append한다. key & value

stack = []

for char in string:
    match char:
        case "+":
            stack.append(stack.pop() + stack.pop())
        case "-":
            stack.append(-stack.pop() + stack.pop())
        case "*":
            stack.append(stack.pop() * stack.pop())
        case "/":
            stack.append((1 / stack.pop()) * stack.pop())
        case _:
            stack.append(int(alpha_dict[char]))

print(f"{stack[0]:.2f}") # stack[0] 을 소수점 둘째 자리까지 프린트
'''
# 씨발 이걸 내가했다고

# -나 /는 지금 쓴 것도 맞긴 한데, 가독성 좀 약하니까
# b=pop(), a=pop() 후 a-b, a/b 해줘도 괜찮다.

# 아, alpha_dict[char]는 이미 int구나.

import sys
input = sys.stdin.readline

cnt = int(input())

string = list(input().strip())

alpha_dict = {}

for ch in range(65, 65 + cnt): # A(65)
    alpha = chr(ch)
    num = int(input())
    alpha_dict[alpha] = num # 딕셔너리는 이런식으로 append한다. key & value

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
                stack.append(a / b)
    else:
        stack.append(alpha_dict[char])

print(f"{stack[0]:.2f}") # stack[0] 을 소수점 둘째 자리까지 프린트