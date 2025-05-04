'''
문제
<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때,
이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

예를 들어, 다음과 같이 81개의 수가 주어지면

 	1열	2열	3열	4열	5열	6열	7열	8열	9열
1행	3	23	85	34	17	74	25	52	65
2행	10	7	39	42	88	52	14	72	63
3행	87	42	18	78	53	45	18	84	53
4행	34	28	64	85	12	16	75	36	55
5행	21	77	45	35	28	75	90	76	1
6행	25	87	65	15	28	11	37	28	74
7행	65	27	75	41	7	89	78	64	39
8행	47	47	70	45	23	65	3	41	44
9행	87	13	82	38	31	12	29	29	80
이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

예제 입력 1 
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80
예제 출력 1 
90
5 7
'''

'''
num_list = [list(map(int, input().split())) for _ in range(9)]
# 이건 그냥 외워둡시다.

max_num_list = []
max_index_list = []
for row in num_list:
    max_num_list.append(max(row))
    max_index_list.append(row.index(max(row)))

max_num = max(max_num_list)

print(max_num)
print(max_num_list.index(max_num) + 1, max_index_list[max_num_list.index(max_num)] + 1)
'''

# 최적화 해봅시다. 전체를 한번에 훑는 방식.

num_list = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if num_list[i][j] > max_num:
            max_num = num_list[i][j]
            max_row = i
            max_col = j

print(max_num)
print(max_row + 1, max_col + 1)


# 리스트 평탄화로 더 간단하게 풀기

'''
num_list = []
for i in range(9):
    num_list += list(map(int, input().split())) # 길이 81짜리 리스트 생성

max_num = max(num_list)
row, col = divmod(num_list.index(max_num), 9) # 인덱스를 9로 나누면 몫이 행이고 나머지가 열이다
print(max_num)
print(row + 1, col + 1)
'''