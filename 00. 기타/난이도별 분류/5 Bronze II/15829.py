'''
입력
첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.

입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.

출력
문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.

Small (50점)
1 ≤ L ≤ 5
Large (50점)
1 ≤ L ≤ 50
예제 입력 1 
5
abcde
예제 출력 1 
4739715
예제 입력 2
3
zzz
예제 출력 2 
25818
예제 입력 3 
1
i
예제 출력 3 
9
힌트
예제 1: abcde의 해시 값은1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314
= 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.

예제 2: zzz의 해시 값은 26 × 310 + 26 × 311 + 26 × 312 = 26 + 806 + 24986 = 25818이다.
'''
'''
L = int(input())
string = input()

alpha = "abcdefghijklmnopqrstuvwxyz"

answer = 0
for i, char in enumerate(string):
    answer += (alpha.index(char) + 1) * (31 ** i)

print(answer)
'''
# 50점이라고? L이 50일때 이게 틀리는 코드라고?

L = int(input())
string = input()

alpha = "abcdefghijklmnopqrstuvwxyz"

answer = 0
for i, char in enumerate(string):
    answer += ((alpha.index(char) + 1) * (31 ** i)) % 1234567891

print(answer % 1234567891)

# 아, 1234567891로 나누라고 써 있구나......
# 문제를 똑띠 읽는 사람이 되자.