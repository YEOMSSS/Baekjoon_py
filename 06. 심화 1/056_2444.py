'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

예제 입력 1 
5
예제 출력 1 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

# cnt = int(input())
# for i in range(1 - cnt, cnt, 1):
#     print(' '*abs(i) + '*'*abs(1 - 2*cnt + 2*abs(i)))
# 되는 건 알겠는데 너무 어렵다. 생각해내기 좀 빡센데.
# abs()는 절댓값을 반환한다.


# cnt = int(input())

# for i in range(cnt):
#     print(" " * (cnt - 1 - i), end = "")
#     print("*" * (2 * i + 1))
# for j in range(cnt - 1):
#     print(" " * (j + 1), end = "")
#     print("*" * (2 * (cnt - 1 - j) - 1)) 

# 그냥 보이는 대로 작성한 코드.
# 잘 돌아가긴 하는데, 뭔가 뭔가다. 뭔가.


# cnt = int(input())

# for i in range(cnt):
#     print(" " * (cnt - 1 - i) + "*" * (2 * i + 1))
# for i in range(cnt - 2, -1, -1):
#     print(" " * (cnt - 1 - i) + "*" * (2 * i + 1))

# range(cnt - 2, -1, -1)은 역순 루프다. 위쪽과 대칭을 구성한다.
# cnt - 2, cnt - 3, cnt - 4 ... 0 까지 i에 들어간다.
# 근데 똑같은 게 두 줄 있으니까 좀 그런데.


cnt = int(input())

for i in list(range(cnt)) + list(range(cnt - 2, -1, -1)):
    print(" " * (cnt - 1 - i) + "*" * (2 * i + 1))

# 야, 이렇게도 되는구나? for문은 정말 다양하네.
# 리스트의 요소가 하나씩 들어간다.