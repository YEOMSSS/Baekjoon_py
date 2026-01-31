import sys

input = sys.stdin.readline

# 2를 곱하거나 3으로 나누는 거만 가능하다.
# 모든 입력은 2와 3으로 소인수분해된다. 찌꺼기는 좀 남겠지만
# 2의 제곱은 오름차순, 3의 제곱은 내림차순으로 정렬되어야 한다.


def brute() -> None:
    N = int(input())
    arr = list(map(int, input().split()))

    # 재활용 계속 돌릴 방문 확인용 배열
    visited = [False for _ in range(N)]

    # curr 다음으로 올 수 있는 값이 있는지 검사 후 이동하는 재귀dfs
    # 경로를 찾지 못하면 visited는 원상태로 복귀한다.
    def dfsR(curr, path):

        # 모든 값을 지났다면 종료
        if len(path) == N:
            print(*path)
            sys.exit()

        # 배열을 순회하며 다음에 올 수 있는 숫자를 찾음
        for i in range(N):

            # 이번 경로에 이미 사용한 값
            if visited[i]:
                continue

            # curr * 2 가 존재하는 경우
            if arr[i] == curr * 2:
                visited[i] = True
                dfsR(arr[i], path + [arr[i]])
                visited[i] = False

            # curr // 3 이 존재하는 경우
            elif curr % 3 == 0 and arr[i] == curr // 3:
                visited[i] = True
                dfsR(arr[i], path + [arr[i]])
                visited[i] = False

    # 모든 숫자를 시작점으로 브루트포스
    for i in range(N):
        visited[i] = True
        dfsR(arr[i], [arr[i]])
        visited[i] = False


def main() -> None:
    N = int(input())
    # 중복되는 값은 절대 입력되지 않는다.
    arr = set(map(int, input().split()))

    result = set()

    for num in arr:
        cnt2 = 0
        cnt3 = 0

        # 소인수분해
        while num % 2 == 0:
            cnt2 += 1
            num //= 2

        while num % 3 == 0:
            cnt3 += 1
            num //= 3

        # 남은 찌꺼기
        rest = num

        result.add((cnt2, cnt3, rest))

    # cnt2와 cnt3 중 뭘 우선으로 정렬해도 상관없다.

    # cnt3 기준 내림차순 우선 후 동일시 cnt2 기준 오름차순
    for cnt2, cnt3, rest in sorted(result, key=lambda x: (-x[1], x[0])):
        print(2**cnt2 * 3**cnt3 * rest, end=" ")

    # cnt2 기준 오름차순 우선 후 동일시 cnt3 기준 내림차순
    # for cnt2, cnt3, rest in sorted(result, key=lambda x: (x[0], -x[1])):
    #     print(2**cnt2 * 3**cnt3 * rest, end=" ")


if __name__ == "__main__":
    # main()
    brute()
