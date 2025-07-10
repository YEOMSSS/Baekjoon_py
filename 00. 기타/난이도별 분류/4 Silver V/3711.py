'''
문제
Z 대학교 학생은 입학할 때 학번을 받게 된다.
학번은 0보다 크거나 같고, 106-1보다 작거나 같은 정수이다.
Z 대학의 김상근 교수는 학번으로 학생들을 구분한다. 
상근이는 학생들을 조금 더 쉽게 기억하기 위해서 자신이 가르치는 학생들의 학번을 m으로 나누었을 때,
나머지가 모두 다른 가장 작은 양의 정수를 찾으려고 한다.

입력
첫째 줄에 테스트 케이스의 개수 N이 주어진다.
각 테스트 케이스의 첫째 줄에는 상근이가 가르치는 학생의 수 G가 (1 ≤ G ≤ 300) 주어진다.
다음 G개 줄에는 학생의 학번이 한 줄에 하나씩 주어진다. 학번이 같은 경우는 없다.

출력
각 테스트 케이스마다, 학번을 m으로 나눈 나머지가 모두 다른 가장 작은 정수 m을 출력한다.

예제 입력 1 
2
1
124866
3
124866
111111
987651
예제 출력 1 
1
8
'''

import sys
input = sys.stdin.readline

def main():
    N = int(input())

    for _ in range(N):
        G = int(input())
        students = [int(input()) for _ in range(G)]

        i = 0
        while True:
            i += 1
            remainders = set()
            for student in students:
                remainders.add(student % i)
            if len(remainders) == G:
                print(i)
                break

if __name__ == "__main__":
    main()