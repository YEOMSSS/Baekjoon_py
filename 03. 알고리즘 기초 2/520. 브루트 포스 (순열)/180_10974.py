'''
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

예제 입력 1 
3
예제 출력 1 
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
'''
def main():

    N = int(input())
    used = [False] * (N + 1)
    result = []

    def backtrack():
        if len(result) == N:
            print(*result)
            return
        
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = True
                result.append(i)
                backtrack()
                result.pop()
                used[i] = False

    backtrack()

if __name__ == "__main__":
    main()
'''
# 내장함수로

from itertools import permutations

def main():

    N = int(input())
    for perm in permutations(range(1, N + 1), N):
        print(*perm)

if __name__ == "__main__":
    main()