'''
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
'''
'''
예제 입력 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
예제 출력 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''
# 일단 생각나는대로. 정답은 뱉지만 메모리가 초과될 듯
# 그래도 나름 set()이라고, PyPy3으로 제출하니 통과된다.
'''
import sys
input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    operation = input().split()
    match operation[0]:
        case "add":
            S.add(operation[1])
        case "remove":
            S.discard(operation[1])
        case "check":
            if operation[1] in S:
                print(1)
            else:
                print(0)
        case "toggle":
            if operation[1] in S:
                S.discard(operation[1])
            else:
                S.add(operation[1])
        case "all":
            S = set(map(str, range(1, 21)))
        case "empty":
            S = set()
'''
# 메모리가 4MB밖에 주어지지 않았다.
# 비트마스크란 무엇인가?

import sys
input = sys.stdin.readline

S = 0  # 20비트만 사용하는 비트마스크. 정수 하나로 숫자 20개 관리
M = int(input())

# 1 << k : 2진수로 1은 0...01이니까, << 왼쪽으로 k칸 비트를 밀면 k번째 비트가 켜진다.
for _ in range(M):
    # 한 줄씩 입력을 읽고 바로 처리하는 구조가 메모리 초과가 안 난다.
    parts = input().split()
    
    match parts[0]:
        case "add":
            # |는 or연산. 자리별로 계산해서 둘중하나가 1이면 1 둘다0이면 0    
            # 0b100 | 0b001 == 0b101. 꺼져있던게 켜짐
            S |= (1 << int(parts[1]) - 1)
        case "remove":
            # &는 and연산. 자리별로 계산해서 둘다1이면 1 아니면 0
            # ~는 not연산. 모든 비트 뒤집기
            # 0b101 & 0b110 == 0b100. 원래 1인건 그대로 1이고 끌것만 0됨
            S &= ~(1 << int(parts[1]) - 1)
        case "check":
            # S에 and연산으로 하나만 켜진 비트를 넣어 True면 1을 print 아니면 0
            # 비트를 출력하는 것보다 이게 더 효율적이다.
            print(1 if S & (1 << int(parts[1]) - 1) else 0)
        case "toggle":
            # ^는 xor연산. 자리별로 계산해서 같으면 0 다르면 1
            # 0b101 ^ 0b001 == 0b100. 기존 자리에 ^0이 된다 해서 변화가 없다.
            S ^= (1 << int(parts[1]) - 1)
        case "all":
            # 21번 비트만 켜두고 거기서 1을 빼면 21이 꺼지고 1~20이 켜진다.
            S = (1 << 20) - 1
        case "empty":
            S = 0
