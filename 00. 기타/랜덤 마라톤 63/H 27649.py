
import sys
input = sys.stdin.readline

strings = input().split()

result = []
prev = ""
for string in strings:
    new_string = list(string)
    for i, char in enumerate(new_string):
        match char:
            case "<":
                new_string[i] = " < "
            case ">":
                new_string[i] = " > "
            case "(":
                new_string[i] = " ( "
            case ")":
                new_string[i] = " ) "
            case "&":
                if prev == char:
                    new_string[i] = " && "
                    prev = ""
                else:
                    new_string[i] = ""
                    prev = "&"
            case "|":
                if prev == char:
                    new_string[i] = " || "
                    prev = ""
                else:
                    new_string[i] = ""
                    prev = "|"

    result.append("".join(new_string))

print(*(" ".join(result)).split())

# 문자열 +=으로 아예 새로만드는 방식은 시간초과를 주의하자.