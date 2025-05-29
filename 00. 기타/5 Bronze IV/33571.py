'''
입력
첫 번째 줄에 디미고 홍보 책자의 글을 나타내는 문자열 $S$가 주어진다. 
$S$는 공백으로 시작하거나 끝나지 않으며, 디미고 로고는 @로 주어진다. $(1\leq |S|\leq 1\,000)$ 

출력
$S$에 있는 글자 속 구멍 개수를 출력한다.

예제 입력 1 
dimigo is the best high school @
예제 출력 1 
10
예제 입력 2 
BBBBBB
예제 출력 2 
12
'''

string = input()

answer = 0
for char in string:
    if char == "B":
        answer += 2
    elif char in ["A", "a", "b", "D", "d", "e", "g",
                  "O", "o", "P", "p", "Q", "q", "R", "@"]:
        # 이런거 할때는 list보다 set이 더 좋댑니다. 
        # 아니? 요소가 적으니까 list가 더 빠르다 이거야.
        # 그냥 백준 서버가 이상한거같아...
        answer += 1
print(answer)