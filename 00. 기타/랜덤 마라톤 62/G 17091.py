'''
문제
단어 시계는 시각을 단어를 이용해서 표현하는 시계이다. 다음은 몇 가지 예시이다.

5:00 → five o' clock
5:01 → one minute past five
5:10 → ten minutes past five
5:15 → quarter past five
5:28 → twenty eight minutes past five
5:30 → half past five
5:40 → twenty minutes to six
5:45 → quarter to six
5:47 → thirteen minutes to six
분 = 0이면 "o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 < 분이면 "to" 를 사용한다.

시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.

입력
첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12), 둘째 줄에 분을 나타내는 m(0 ≤ m < 60)이 주어진다.

출력
첫째 줄에 입력으로 주어진 시각을 단어 시계에서 사용하는 표현으로 출력한다.
'''

# 5
# 47
# thirteen minutes to six

H = int(input())
M = int(input())
if 30 < M:
    if H == 12:
        H = 1
    else:
        H += 1

result_H = ""
result_M = ""

match H:
    case 1:
        result_H = "one"
    case 2:
        result_H = "two"
    case 3:
        result_H = "three"
    case 4:
        result_H = "four"
    case 5:
        result_H = "five"
    case 6:
        result_H = "six"
    case 7:
        result_H = "seven"
    case 8:
        result_H = "eight"
    case 9:
        result_H = "nine"
    case 10:
        result_H = "ten"
    case 11:
        result_H = "eleven"
    case 12:
        result_H = "twelve"

match M:
    case 0:
        result_M = "o' clock"
    case 1 | 59:
        result_M = "one minute"
    case 2 | 58:
        result_M = "two minutes"
    case 3 | 57:
        result_M = "three minutes"
    case 4 | 56:
        result_M = "four minutes"
    case 5 | 55:
        result_M = "five minutes"
    case 6 | 54:
        result_M = "six minutes"
    case 7 | 53:
        result_M = "seven minutes"
    case 8 | 52:
        result_M = "eight minutes"
    case 9 | 51:
        result_M = "nine minutes"
    case 10 | 50:
        result_M = "ten minutes"
    case 11 | 49:
        result_M = "eleven minutes"
    case 12 | 48:
        result_M = "twelve minutes"
    case 13 | 47:
        result_M = "thirteen minutes"
    case 14 | 46:
        result_M = "fourteen minutes"
    case 15 | 45:
        result_M = "quarter"
    case 16 | 44:
        result_M = "sixteen minutes"
    case 17 | 43:
        result_M = "seventeen minutes"
    case 18 | 42:
        result_M = "eighteen minutes"
    case 19 | 41:
        result_M = "nineteen minutes"
    case 20 | 40:
        result_M = "twenty minutes"
    case 21 | 39:
        result_M = "twenty one minutes"
    case 22 | 38:
        result_M = "twenty two minutes"
    case 23 | 37:
        result_M = "twenty three minutes"
    case 24 | 36:
        result_M = "twenty four minutes"
    case 25 | 35:
        result_M = "twenty five minutes"
    case 26 | 34:
        result_M = "twenty six minutes"
    case 27 | 33:
        result_M = "twenty seven minutes"
    case 28 | 32:
        result_M = "twenty eight minutes"
    case 29 | 31:
        result_M = "twenty nine minutes"
    case 30:
        result_M = "half"

if M == 0:
    print(result_H, result_M)
elif 1 <= M <= 30:
    print(result_M, "past", result_H)
elif 30 < M:
    print(result_M, "to", result_H)