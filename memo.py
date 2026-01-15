answer = [0, 0, 0]


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


if __name__ == "__main__":
    main()
