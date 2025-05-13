'''
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

예제 입력 1 
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
예제 출력 1 
4 4 4
6 6 6
5 6 100
'''

N, M = map(int, input().split())

# matrix1 = []
# for _ in range(N):
#     matrix1.append(list(map(int, input().split())))

# matrix2 = []
# for _ in range(N):
#     matrix2.append(list(map(int, input().split())))

# 이런 거 할 때 def 쓰라고
def matrix_maker(row):
    matrix = []
    for _ in range(row):
        matrix.append(list(map(int, input().split())))
    return matrix

# return [list(map(int, input().split())) for _ in range(row)]
# 이걸로 쓰면 matrix_maker는 한줄로 원콤.

matrix1 = matrix_maker(N)
matrix2 = matrix_maker(N)

result = []
for i in range(N):
    result.append([])
    for j in range(M):
        result[i].append(matrix1[i][j] + matrix2[i][j])

# result = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)]

for row in result:
    print(*row)



# 리얼 진짜 짧게 만든 코드
'''
N, M = map(int, input().split())

def matrix_maker(row):
    return [list(map(int, input().split())) for _ in range(row)]

matrix1 = matrix_maker(N)
matrix2 = matrix_maker(N)

result = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)]

for row in result:
    print(*row)
'''