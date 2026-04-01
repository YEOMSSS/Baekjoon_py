# 괄호로만 이루어진 데이터라 치고...
Data = "<>{}()))"

stack = []
answer = 1

for ch in Data:
    # 열린괄호가 입력되면 push
    if ch in "{<[(":
        stack.append(ch)

    # stack이 비었는데 닫힌괄호가 입력되면 비정상
    elif not stack:
        answer = 0
        break

    # stack이 차 있을 때 닫힌괄호가 입력되면 짝맞추기
    elif (
        (ch in ")" and stack[-1] == "(")
        or (ch in "]" and stack[-1] == "[")
        or (ch in "}" and stack[-1] == "{")
        or (ch in ">" and stack[-1] == "<")
    ):
        stack.pop()

    # 짝이 안맞으면 비정상
    else:
        answer = 0
        break

if stack:
    answer = 0

print(answer)
