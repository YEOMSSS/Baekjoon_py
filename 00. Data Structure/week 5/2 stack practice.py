msg = "Data"

stack = []
for ch in msg:
    stack.append(ch)

while stack:
    print(stack.pop(), end=" ")
