Data = list("<>{}()")

stack = []

pare = {">": "<", "}": "{", ")": "(", "]": "["}
answer = 0

is_matched = True  # Flag가 필요한가?

while Data:
    ch = Data.pop(0)  # data가 list여야 한다.

    if ch in pare.values():  # dict의 value만 모아놓은 것
        stack.append(ch)
    elif stack and pare[ch] == stack[-1]:
        stack.pop()
    else:
        is_matched = False
        break


if is_matched and not stack:
    answer = 1

print(answer)
