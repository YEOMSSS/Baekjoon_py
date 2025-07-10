'''
-는 0에 대응한다.
\는 1에 대응한다.
(는 2에 대응한다.
@는 3에 대응한다.
?는 4에 대응한다.
>는 5에 대응한다.
&는 6에 대응한다.
%는 7에 대응한다.
/는 -1에 대응한다.
'''

import sys
input = sys.stdin.readline

while True:
    octopus = input().rstrip()
    if octopus == "#":
        break
    str_num = ""
    for sign in octopus:
        match sign:
            case "-":
                str_num += "0"
            case "\\":
                str_num += "1"
            case "(":
                str_num += "2"
            case "@":
                str_num += "3"
            case "?":
                str_num += "4"
            case ">":
                str_num += "5"
            case "&":
                str_num += "6"
            case "%":
                str_num += "7"
            case "/":
                str_num += "-"

    result = 0    
    for idx, num in enumerate(str_num[::-1]):
        if num == "-":
            result += 8 ** idx * -1
        else:
            result += 8 ** idx * int(num)

    print(result)