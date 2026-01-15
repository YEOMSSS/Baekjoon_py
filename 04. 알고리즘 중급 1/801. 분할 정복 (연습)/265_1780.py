import sys

input = sys.stdin.readline


answer = [0, 0, 0]


# 슬라이싱과 set을 사용하지 않는 형태
def main() -> None:
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 슬라이싱 없이 고정된 arr에 재귀
    def func_R(x, y, n):
        first = arr[x][y]
        same = True

        # 모든 원소를 좌상단 원소와 직접 비교
        for i in range(x, x + n):
            for j in range(y, y + n):

                if arr[i][j] != first:
                    same = False
                    break

            if not same:
                break

        # 동일할 경우 재귀 종료
        if same:
            answer[first + 1] += 1
            return

        # 동일하지 않은 경우 9회 추가 재귀
        d3 = n // 3
        for dx in range(3):
            for dy in range(3):
                func_R(x + dx * d3, y + dy * d3, d3)

    func_R(0, 0, N)

    for a in answer:
        print(a)


# def is_same(arr: list) -> bool:

#     prev = arr[0][0]
#     for a in arr:
#         if not len(set(a)) == 1:
#             return False
#         if not prev == a[0]:
#             return False
#         prev = a[0]

#     return True


# def func_R(arr: list, n: int) -> None:
#     # print(arr)
#     if is_same(arr):
#         answer[arr[0][0] + 1] += 1
#         return

#     d3 = n // 3
#     if not d3:
#         return

#     # 상단 3개
#     func_R([arr[i][:d3] for i in range(d3)], d3)
#     func_R([arr[i][d3 : d3 * 2] for i in range(d3)], d3)
#     func_R([arr[i][d3 * 2 :] for i in range(d3)], d3)
#     # 중앙 3개
#     func_R([arr[i][:d3] for i in range(d3, d3 * 2)], d3)
#     func_R([arr[i][d3 : d3 * 2] for i in range(d3, d3 * 2)], d3)
#     func_R([arr[i][d3 * 2 :] for i in range(d3, d3 * 2)], d3)
#     # 하단 3개
#     func_R([arr[i][:d3] for i in range(d3 * 2, n)], d3)
#     func_R([arr[i][d3 : d3 * 2] for i in range(d3 * 2, n)], d3)
#     func_R([arr[i][d3 * 2 :] for i in range(d3 * 2, n)], d3)


# def main() -> None:
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     func_R(arr, N)

#     for a in answer:
#         print(a)


if __name__ == "__main__":
    main()
