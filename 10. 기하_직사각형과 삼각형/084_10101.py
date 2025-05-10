'''
문제
창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

삼각형의 세 각을 입력받은 다음,

세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.

입력
총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.

출력
문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.

예제 입력 1 
60
70
50
예제 출력 1 
Scalene
'''
'''
ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

if not ang1 + ang2 + ang3 == 180:
    print("Error")
elif ang1 == ang2 == ang3:
    print("Equilateral")
elif ang1 == ang2 or ang2 == ang3 or ang1 == ang3:
    print("Isosceles")
else:
    print("Scalene")
'''
# 너무 직관적이라 해야 할까? 좀 더 고급지게?

angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
    print("Error")
elif len(set(angles)) == 1:
    print("Equilateral")
elif len(set(angles)) == 2:
    print("Isosceles")
else:
    print("Scalene")

# 존나 잘하는데? len(set(arr)) 좀 지리는데?
# 근데 웃기는건 첨에 한한게 직관적이라 4ms 더 빠르다는거. ㅋㅋㅋ