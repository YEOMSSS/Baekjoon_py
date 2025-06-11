'''
import sys
input = sys.stdin.readline

def main():

    T = int(input())

    for _ in range(T):
        M, N, x, y = map(int, input().split())

        # 유클리드: b가 0일때 a가 GCD
        a, b = M, N
        while b != 0:
            a, b = b, a % b
        LCM = (M * N) // a


        for i in range(1, LCM + 1):
            
            check_x = i % M if i % M != 0 else M
            check_y = i % N if i % N != 0 else N

            if check_x == x and check_y == y:
                print(i)
                break
        else:
            print(-1)

if __name__ == "__main__":
    main()
'''
# 시간 초과.
# 굳이 1~LCM을 전부 확인해야 할까?
# M의 배수 + x만 확인해봐도 되지 않을까? N의 배수 + y를 해봐도 되고.


import sys
input = sys.stdin.readline

def main():

    T = int(input())

    for _ in range(T):
        M, N, x, y = map(int, input().split())

        # 최소공배수 구하기
        a, b = M, N
        while b != 0:
            a, b = b, a % b
        LCM = (M * N) // a

        # x가 맞을때의 값을 y에 대입해보기
        i = 0
        while M * i + x <= LCM:
            if (M * i + x) % N == y or ((M * i + x) % N == 0 and N == y):
                print(M * i + x)
                break
            i += 1
        else:
            print(-1)

if __name__ == "__main__":
    main()