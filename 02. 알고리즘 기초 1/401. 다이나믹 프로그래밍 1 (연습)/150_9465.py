'''
문제
상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다.
스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다.
상냥이는 스티커를 이용해 책상을 꾸미려고 한다.

상냥이가 구매한 스티커의 품질은 매우 좋지 않다.
스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.

모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고,
점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다.
상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오.
즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 
점수는 260이 되고 이 것이 최대 점수이다. 
가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다. 
다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 
연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다. 

출력
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.

예제 입력 1 
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
예제 출력 1 
260
290
'''
# 오른쪽으로 가면서 더해야 하겠다.
# 경우의 수는, 앞칸을 선택하지 않거나 하거나 둘 중 하나다.
# 두 칸을 떼는 경우는 없으니까.

# 윗줄을 0, 아랫줄을 1라고 하면
# 앞칸에서 0을 선택하면 이번칸은 1, prev가 1면 new는 0.
# prev가 비어있으면 new는 둘중에 max.

# 그럼 경우는 세 가지다.
# 빈 prev + max(new)
# prev 0 + new 1, prev 1 + new 0
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    UPP_list = list(map(int, input().split()))
    LOW_list = list(map(int, input().split()))
    
    if N == 1:
        print(max(UPP_list[0], LOW_list[0]))
        continue

    dp = [[0] * 3 for _ in range(N + 1)]
    dp[1] = [max(UPP_list[0], LOW_list[0]), UPP_list[0], LOW_list[0]]

    upp, low = 1, 2
    for i in range(2, N + 1):
        dp[i][0] = max(dp[i - 2][1:]) + max(UPP_list[i - 1], LOW_list[i - 1])
        dp[i][upp] = dp[i - 1][low] + UPP_list[i - 1]
        dp[i][low] = dp[i - 1][upp] + LOW_list[i - 1]

    # print(dp)
    print(max(dp[N]))
'''
# 이 코드는 틀렸다.
# dp[i][0] 은 존재할 필요가 없다.
# 빈칸으로 끝나는 경우가 없는데, 어떻게 빈칸으로 끝나는 경우를 저장해?
# 한칸 건너뛴 경우가 존재하지 않는 칸에 저장되기에 답을 출력할 수 없다.
# 다시!
# 반례 : 답은 7이나 코드는 6을 출력.
# 1
# 4
# 1 1 2 1
# 3 1 1 2
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    # if N == 1:
    #     print(max(U[0], D[0]))
    #     continue

    dp = [[0, 0] for _ in range(N + 1)]
    dp[1] = [U[0], D[0]]

    u, d = 0, 1
    for i in range(2, N + 1):
        prev2_max = max(dp[i - 2])
        dp[i][u] = max(dp[i - 1][d] + U[i - 1], prev2_max + U[i - 1])
        dp[i][d] = max(dp[i - 1][u] + D[i - 1], prev2_max + D[i - 1])

    print(max(dp[N]))
'''
# 공간 최적화 되겠는데?
# 이전과 그 이전까지 사용하니 변수 4개로 돌려야한다.

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    U = list(map(int, input().split()))
    D = list(map(int, input().split()))

    prev_u, prev_d = 0, 0
    curr_u, curr_d = U[0], D[0]
    
    for i in range(1, N):
        new_u = max(curr_d + U[i], max(prev_u, prev_d) + U[i])
        new_d = max(curr_u + D[i], max(prev_u, prev_d) + D[i])

        prev_u, prev_d = curr_u, curr_d
        curr_u, curr_d = new_u, new_d

    print(max(curr_u, curr_d))
