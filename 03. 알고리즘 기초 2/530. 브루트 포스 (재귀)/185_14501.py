'''
문제
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다.
5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.
예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다.
2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며,
이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며,
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
'''
'''
예제 입력 1 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
예제 출력 1 
45
예제 입력 2 
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
예제 출력 2 
55
예제 입력 3 
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
1 6
예제 출력 3 
20
예제 입력 4 
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
예제 출력 4 
90
'''

# Ti의 합이 N 이하일 때를 찾으면 될 듯.
# 하나 집으면 그 다음은 당일+Ti부터 또 돌리면 될 듯.
'''
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    Ti_and_Pi = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0

    def backtrack(day, profit):
        nonlocal max_result

        # 날짜가 넘어가면 종료
        if day >= N:
            max_result = max(max_result, profit)
            return

        Ti, Pi = Ti_and_Pi[day]

        if day + Ti <= N: # 업무를 맡는 경우
            backtrack(day + Ti, profit + Pi)

        backtrack(day + 1, profit) # 업무를 안 맡는 경우 (for문의 역할)

    backtrack(0, 0)
    print(max_result)

if __name__ == "__main__":
    main()
'''
# dp로도 풀어보자. 점화식이 큰수부터 풀어야하는구나.
'''
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    Ti_and_Pi = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (N + 1) # 그냥 N일 경우 마지막 Ti가 1일때 max가 빈다.

    # 점화식이 거꾸로 간다!!
    for i in range(N - 1, -1, -1):
        Ti, Pi = Ti_and_Pi[i]

        # i업무 마친 다음날 이후부터 벌수있는 최댓값
        if Ti + i <= N:
            dp[i] = Pi + max(dp[i + Ti :])

    print(dp)

if __name__ == "__main__":
    main()
'''
# 순서대로 넣어도 풀 수 있다??
# 생각해내기 엄청나게 어렵다. 봐도어렵네. 아니 모르겠다.
# 겨우 겨우 이해했네, 로직이 존나 어렵다 이걸 어떻게 생각해내는 거냐

import sys
input = sys.stdin.readline

def main():
    N = int(input())

    dp = [0] * (N + 1)

    for i in range(N):
        Ti, Pi = map(int, input().split())

        # 오늘까지 일한 날의 초기값, 어제까지 일한 값
        dp[i + 1] = max(dp[i + 1], dp[i])

        # 오늘일까지 끝낸 날의 초기값, 어제까지 일한 값에 오늘일 끝낸거까지 합한 값
        if i + Ti <= N: # 오늘일 끝내도 날짜 초과 안되면 실행
            dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)

    print(dp[N])

if __name__ == "__main__":
    main()