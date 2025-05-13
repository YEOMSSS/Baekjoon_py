'''
문제
오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
입력
첫째 줄에 입력의 크기 n(1 ≤ n ≤ 500,000)이 주어진다.

출력
첫째 줄에 코드1 의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다.
단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

예제 입력 1 
7
예제 출력 1 
35
3
코드1 이 35회 수행되고 알고리즘의 수행 시간이 n3에 비례한다.
'''
# 수식이 정리된 코드
'''
size = int(input())

cnt = (size - 1) * (size) * (size - 2) // 6
degree = 3

print(cnt)
print(degree)
'''
# for i in range(1, n - 1)
# for j in range(i + 1, n)
# for k in range(j + 1, n + 1)

# n 들어가는 반복문 세번이면 시간복잡도는 O(n^3)이지 뭐.

size = int(input())

cnt = (size - 1) * (size) * (size - 2) // 6 # 시그마 (n-1)(n-2)/2
# for i in range(1, size - 1):
#     # 7-2 7-3 7-4 7-5 7-6
#     # 7-3 7-4 7-5 7-6
#     # 7-4 7-5 7-6
#     # 7-5 7-6
#     # 7-6
#     # 5 4 3 2 1 i=1 size-i-1=5
#     # 4 3 2 1 i=2 size-i-1=4
#     # 3 2 1 i=3
#     # 2 1 i=4
#     # 1 i=5
#     # (size-i-1+1) * (size-i-1) / 2
#     cnt += (size - i) * (size - i - 1) / 2 # (n-1)(n-2)/2
#     # for j in range(i + 1, size):
#     #     cnt += size - j
#     #     # for k in range(j + 1, size + 1):
#     #     #     cnt += 1
degree = 3

print(cnt)
print(degree)

# 밑에 거, 왜 틀렸을까?
'''
size = int(input())
cnt = 0
for i in range(1, size - 1):    
    cnt += (size - i) * (size - i - 1) / 2
print(int(cnt))
print(3)
'''
# int(cnt)에서 버림을 사용하기 때문에 부동소수점 오차가 난다.
# 애초에 정수 계산할 때 //를 사용해야 하는 거였다.
'''
size = int(input())
cnt = 0
for i in range(1, size - 1):    
    cnt += (size - i) * (size - i - 1) // 2
print(cnt)
print(3)
'''
# 이렇게 쓰면 되겠다.

# 씨발 진짜 무슨 수학을 처 하고있네.
# 개 좆같은 시그마 공부를 또 하라고?