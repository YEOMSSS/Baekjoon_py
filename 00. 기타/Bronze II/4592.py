'''
입력
각 줄마다 처음으로 정수 N(0 < N ≤ 25)이 주어진다.  그 다음 N개에 걸쳐 1부터 99 사이의 수가 주어진다.

마지막 줄에 입력의 끝을 알리는 0이 주어진다.

출력
각 케이스마다 한 줄씩 연속하는 중복을 제거한 원래의 제출 상태를 출력한다.

각 줄의 마지막에는 한 칸을 띄고 '$' 표시가 붙는다.

예제 입력 1 
5 1 22 22 22 3
4 98 76 20 76
6 19 19 35 86 86 86
1 7
0
예제 출력 1 
1 22 3 $
98 76 20 76 $
19 35 86 $
7 $
'''

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    answer = [nums[1]]
    for num in nums[2:]:
        if answer[-1] != num:
            answer.append(num)
    print(*answer, "$")