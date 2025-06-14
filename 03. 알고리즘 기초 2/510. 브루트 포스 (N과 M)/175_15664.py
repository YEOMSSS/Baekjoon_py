'''
문제
N개의 자연수와 자연수 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4
예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 7
1 9
7 9
9 9
예제 입력 3 
4 4
1 1 2 2
예제 출력 3 
1 1 2 2
'''

# 중복금지이므로 스위치 필요
# 비내림차순이면 start 가 필요
# N에 같은 수가 올 수 있기에 prev 필요

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    nums = sorted(list(map(int, input().split())))
    used = [False] * N
    result = []

    def backtrack(start):
        if len(result) == M:
            print(*result)
            return

        prev = -1
        for i in range(start, len(nums)):
            if not used[i] and prev != nums[i]:
                used[i] = True
                result.append(nums[i])
                prev = nums[i]
                backtrack(i)
                result.pop()
                used[i] = False

    backtrack(0)

if __name__ == "__main__":
    main()