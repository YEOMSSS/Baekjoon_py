'''
문제
N개의 정수로 이루어진 배열 A가 주어진다.
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다.
둘째 줄에는 배열 A에 들어있는 정수가 주어진다.
배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

예제 입력 1 
6
20 1 15 8 4 10
예제 출력 1 
62
'''

# 중복은 허용치 않으니 used 쓰고
# arr에 같은게 들어올 수 있으니 prev 쓰고
# 순열구하는거니까 start는 필요없다.

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    used = [False] * N
    result = []
    answer = set()

    def backtrack():
        if len(result) == N:
            total = 0
            for i in range(N - 1):
                total += abs(result[i] - result[i + 1])
            answer.add(total)
            return
        
        prev = -1
        for i in range(N):
            num = arr[i]

            if not used[i] and prev != num:
                used[i] = True
                result.append(num)
                prev = num
                backtrack()
                result.pop()
                used[i] = False

    backtrack()
    print(max(answer))

if __name__ == "__main__":
    main()