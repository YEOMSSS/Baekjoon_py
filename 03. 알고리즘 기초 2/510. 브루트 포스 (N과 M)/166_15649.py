'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
'''
예제 입력 1 
3 1
예제 출력 1 
1
2
3
예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
'''
'''
from itertools import permutations

def main():

    N, M = map(int, input().split())

    N_list = list(range(1, N + 1))

    perms = list(permutations(N_list, M))

    for perm in perms:
        print(*perm)

if __name__ == "__main__":
    main()
'''
# 백트래킹을 사용해보자.

def main():

    N, M = map(int, input().split())
    used = [False] * (N + 1)  # 숫자마다 스위치 달아주기 (사용 여부 판단용)
    result = []  # 순열 저장용

    def backtrack():
        # 순열 다 차면 출력
        if len(result) == M:
            print(*result)
            return

        for i in range(1, N + 1):
            if not used[i]:  # i 스위치 꺼져있으면
                used[i] = True  # i 스위치 켜기
                result.append(i)  # i를 perm에 추가
                backtrack()  # 남은 숫자들 중 작은거 넣기
                result.pop()  # 재귀가 끝나고, 순열에서 마지막 숫자 제거
                used[i] = False  # i 스위치 끄기

    backtrack()  # 백트래킹 시작

if __name__ == "__main__":
    main()
