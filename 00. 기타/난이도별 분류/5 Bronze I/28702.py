'''
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
'''

# 무조건 숫자가 하나는 들어올 수밖에 없다는 것을알 면쉽다.

strings = [input() for _ in range(3)]

for i, string in enumerate(strings):
    if string.isdigit():
        result = (int(string) + 3 - i)

if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)