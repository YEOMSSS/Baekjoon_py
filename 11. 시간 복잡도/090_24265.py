'''
문제
오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
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
21
2
코드1 이 21회 수행되고 알고리즘의 수행 시간이 n2에 비례한다.
'''

# 서준아 좀 닥쳐

# 이번엔 ManOfPassion에서 n의 반복 횟수가 바뀌었다.
# for i in range(1, n) for j in range(i + 1, n + 1)이다.
# 수행 횟수를 구해보자.

# 결국 반복문이 두 번이니 시간복잡도는 O(n^2)이다.

size = int(input())
'''
# O(n^2)의 방법
count = 0
for i in range(1, size):
    for j in range(i + 1, size + 1):
        count += 1
'''
'''
# O(n)의 방법
count = 0
for  i in range(1, size):
    count += size - i
'''
# O(1)의 방법
# size = 7이면 1+2+3+4+5+6을 한다. 3.5*6. size / 2 * (size - 1)이다.
# size = 8이면 1+2+3+4+5+6+7. 4*7. 9면 4.5*8.
count = int(size / 2 * (size - 1))
degree = 2 # 시간복잡도가 O(n^2)이다. n의 지수는 2이다.

print(count)
print(degree)
