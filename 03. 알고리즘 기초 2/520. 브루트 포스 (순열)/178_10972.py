'''
문제
1부터 N까지의 수로 이루어진 순열이 있다.
이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고,
가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

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
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다.
만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
1 2 4 3
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
-1
'''

# 1~N으로 이루어진 순열인데 N<=10000이면 모든 조합을 구할 순 없다..

# 재밌는 규칙을 찾았다.
# 순열을 뒤에서부터 순서대로 세서, 계속 커지다가 작아지는 순간까지.
# 예를 들자면 2 1 5 4 3의 다음은 2 3 1 4 5다.
# 1 5 4 3이 해당한다고 할 수 있다.
# 그러면 1보다 크면서 뒤에 있는 애들중에 제일 작은애를 1 자리에 놓고
# 나머지는 정렬해서 그대로 붙여주면 된다는 거.

# 일단 해봐!
'''
import sys
input = sys.stdin.readline

def main():

    N = int(input())

    perm_reversed = list(map(int, input().split()))[::-1]

    prev = -1
    for i, num in enumerate(perm_reversed):
        if prev > num: # 뒤집힌 수열의 진행이 작아지다가 커지는 순간
            target_perm = perm_reversed[: i] # 끝에서부터 커지는 수열 (뒤집힌 상태)

            min_target = 10001
            for target in target_perm: # num 보다 큰 수들 중 가장 작은 수 찾기
                if target > num:
                    min_target = min(min_target, target)

            # print(*perm_reversed[: i : -1], end= " ") # 영향받지 않는 부분
            # print(min_target, end= " ") # 새로 찾은 그다음 수

            target_perm.remove(min_target) # 새로 찾은 수는 사용했으니 뻬고
            target_perm.append(num) # 바뀐 수를 다시 넣어준 후
            target_perm.sort()
            # print(*target_perm) # 정렬해서 출력

            answer = perm_reversed[: i : -1] + [min_target] + target_perm
            print(*answer)

            break
        prev = num

    else:
        print(-1)

if __name__ == "__main__":
    main()
'''
# 뒤집지 말고 그냥 뒤에서부터 세면 안되나?

import sys
input = sys.stdin.readline

def main():

    N = int(input())

    permutation = list(map(int, input().split()))

    prev = -1
    for i in range(N - 1, -1, -1): # 순열의 뒤에서부터 체크
        num = permutation[i]
        if prev > num:
            target_perm = permutation[i + 1 :] # 뒤에서부터 센 커지는 순열
            
            min_target = 10001
            for target in target_perm: # num 보다 큰 수들 중 가장 작은 수 찾기
                if target > num:
                    min_target = min(min_target, target)

            target_perm.remove(min_target) # 새로 찾은 수는 사용했으니 뻬고
            target_perm.append(num) # 바뀐 수를 다시 넣어준 후
            target_perm.sort() # 정렬한다.

            answer = permutation[: i] + [min_target] + target_perm
            print(*answer)

            break
        prev = num

    else:
        print(-1)

if __name__ == "__main__":
    main()

# 잘 풀어냈다!!

# 다른 방법으로는 아예 바꿀 수 두개만 골라내서 바꿔주는 경우도 있는 듯.
# 그래도 뉘앙스는 거의 비슷했으니가, 합격점!