# 1호부터 다 채우고 2호로 넘어간다. 층수는 1층부터 올라간다.
# 1호 * 층수, 2호 * 층수 이런 식으로 쭉 채운다.
# 호수는 층 + 호 로 뽑으면 된다.
'''
import sys
input = sys.stdin.readline

cnt = int(input())
for _ in range(cnt):
    H, W, N = map(int, input().split())
    x = N // H + 1 if N % H != 0 else N // H
    y = N % H if N % H != 0 else H
    print(str(y) + "0" + str(x) if x < 10 else str(y) + str(x))
'''
# GPT를 맹신하지 말란 말이다. x도 나머지가 0일때 바뀌잖아.
# 왜 계속 당하는 거야. 저놈은 정답이 아니라 힌트맨이다.
# 저놈한테 검사받고 칭찬받아봤자 아무 의미가 없다.
# 얘한테는 모르는거만 물어보는 거지, 오류를 대체 왜 이리 못잡는거야?
'''
import sys
input = sys.stdin.readline

cnt = int(input())
for _ in range(cnt):
    H, W, N = map(int, input().split())
    if N % H == 0:
        x = N // H
        y = H
    else:
        x = N // H + 1
        y = N % H
    print(y * 100 + x)
'''
# 코드를 약간 더 축약해 봐.

import sys
input = sys.stdin.readline

cnt = int(input())
for _ in range(cnt):
    H, W, N = map(int, input().split())
    x = (N - 1) // H + 1
    y = H if N % H == 0 else N % H
    # print(y * 100 + x)
    print(str(y) + "0" + str(x) if x < 10 else str(y) + str(x))

# 빠르긴 첨에 한게 제일 빠르네, 거 참..