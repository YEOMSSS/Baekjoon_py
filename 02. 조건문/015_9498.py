'''
문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.

예제 입력 1 
100
예제 출력 1 
A
'''
def score_calc(x):
    if 90 <= x <= 100:
        print("A")
    elif 80 <= x <= 89:
        print("B")
    elif 70 <= x <= 79:
        print("C")
    elif 60 <= x <= 69:
        print("D")
    else:
        print("F")
# 어차피 위에서 걸러지고 남은거만 있는건데
# 굳이 범위를 저렇게 자세히 해야되나?
# 그냥 90보다큼, 80보다큼, 이런식으로만 써도 됨. 
'''def score_calc(x):
    if 90 <= x <= 100:
        print("A")
    elif 80 <= x:
        print("B")
    elif 70 <= x:
        print("C")
    elif 60 <= x:
        print("D")
    else:
        print("F")'''

score = int(input())

if 0 <= score <= 100:
    score_calc(score)
else:
    print("올바른 수를 입력하세요.")