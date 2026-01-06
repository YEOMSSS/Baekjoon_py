'''
문제
1부터 N까지의 수로 이루어진 순열이 있다.
이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다.
만약, 사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
-1
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
5 4 3 1 2
'''
# 다음 순열 찾기를 그대로 뒤집으면 되겠다.

# 2 3 1 4 5 -> 2 1 5 4 3

import sys
input = sys.stdin.readline

def main():

    N = int(input())

    permutation = list(map(int, input().split()))

    prev = 10001
    for i in range(N - 1, -1, -1): # 순열의 뒤에서부터 체크
        num = permutation[i]
        if prev < num:
            target_perm = permutation[i + 1 :] # 뒤에서부터 센 작아지는 순열
            
            max_target = -1
            for target in target_perm: # num 보다 작은 수들 중 가장 큰 수 찾기
                if target < num:
                    max_target = max(max_target, target)
            
            target_perm.remove(max_target) # 새로 찾은 수는 사용했으니 뻬고
            target_perm.append(num) # 바뀐 수를 다시 넣어준 후
            target_perm.sort() # 정렬 후 뒤집어야한다.

            answer = permutation[: i] + [max_target] + target_perm[::-1]
            print(*answer)

            break
        prev = num

    else:
        print(-1)

if __name__ == "__main__":
    main()
