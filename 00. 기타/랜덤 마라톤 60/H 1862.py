# 9진법이라 생각하면 될듯

numbers = input()

digit = 0
result = 0
for num_str in numbers[::-1]:
    num = int(num_str)
    if num > 4:
        num -= 1
    result += num * (9 ** digit)
    digit += 1

print(result)