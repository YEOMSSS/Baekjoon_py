import sys

input = sys.stdin.readline


# 배열을 몇 번 훑어야 선택정렬이 종료되냐?
# 배열을 한 번 훑을 때마다 젤 큰게 없어진다.

# 1, 3 '2', 5 '4'   2회 32, 54
# 2 '1', 4 '3', 5   2회 21, 43

# 1, 5 2, 4 '3'   3회 543
# 1, 3, 5 '2', 4  3회 352

# 5 4 2 '1', 3    4회 5421
# 4 2, 3 '1', 5   4회 4231

# 자신보다 큰게 앞에 몇개있는지 센다.
# 효율적으로 할라면 내림차순으로 묶어서 제일 작은거에서만 체크하면 되겠다.
# 응, 시간초과야

# 이걸 어떻게 해야 쉽게 할 수 있을까?
# 오른쪽에 있는게 왼쪽으로 가야하는 경우, 한번 갈 때마다 한 턴이 소요된다.
# 그게 자신보다 큰게 앞에 몇개 있는지 세는 것과 같다.
# 그러면 처음 인덱스를 기억해뒀다가, 정렬해서 정렬 위치와 원래 위치를 비교하면
# 이동해야 할 칸수가 나오지 않을까? 굳이 앞에 있는 걸 세지 않더라도.


def main() -> None:
    N = int(input())

    if N == 1:
        print(1)
        return

    # 현재 순서를 저장해서 값 오름차순으로 정렬
    # arr = [(value, idx) for idx, value in enumerate(int(input()) for _ in range(N))]
    arr = []
    for i in range(N):
        arr.append((int(input()), i))

    # 파이썬의 sort는 Timsort로, stable_sort이므로 중복값에도 영향을 받지 않는다.
    # 다만 인덱스가 저장되어 있어서 어차피 기본 sort를 하면 유지되어 정렬되긴 한다.
    # key=lambda x: x[0]으로 앞값만 보게 해도 같은 결과가 나온다는거.
    arr.sort(key=lambda x: x[0])

    answer = 0
    for i in range(N):
        answer = max(arr[i][1] - i, answer)

    print(answer + 1)


def fail() -> None:
    N = int(input())

    if N == 1:
        print(1)
        return

    arr = [int(input()) for _ in range(N)]
    arr_set = set(arr)

    value_to_rank = {value: rank for rank, value in enumerate(sorted(arr_set))}
    compress = [value_to_rank[a] for a in arr]

    counter = [0] * len(arr_set)

    answer = 0
    for i in range(N - 1):
        counter[compress[i]] += 1
        if compress[i] > compress[i + 1]:
            pass
        else:
            answer = max(answer, sum(counter[compress[i] + 1 :]))

    answer = max(answer, sum(counter[compress[N - 1] + 1 :]))

    print(answer + 1)


if __name__ == "__main__":
    main()
