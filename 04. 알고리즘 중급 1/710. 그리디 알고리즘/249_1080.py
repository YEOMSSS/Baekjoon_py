'''
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다.
이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
'''

# 어려워 보이지만, 그냥 3*3의 첫칸을 전부 확인하면 되는 문제다.
# 이건 왜그런지를 이해하는게 힘들지, 코드 자체는 짜기 쉽다.

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    arr1 = [list(map(int, input().rstrip())) for _ in range(N)]
    arr2 = [list(map(int, input().rstrip())) for _ in range(N)]

    cnt = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if arr1[i][j] == arr2[i][j]:
                continue

            for y in range(3):
                for x in range(3):
                    # XOR 연산. 1과 같으면 0 반환, 1과 다르면 1 반환
                    arr1[i + y][j + x] ^= 1
            cnt += 1

    if arr1 == arr2:
        print(cnt)
    else:
        print(-1)

if __name__ ==  "__main__":
    main()
    