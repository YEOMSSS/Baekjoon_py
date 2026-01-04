# 0 1 2 3
# 0을 누르냐 안누르냐로 2가지 가지를 낸다.
# 이후부터는 1을 누르면 0만 바뀌고, 2를 누르면 1만 바뀐다.
# 이런 식으로 앞에서부터 누르면 그리디로 최소거리탐색이 된다.


def main():
    N = int(input())
    current = list(map(int, input()))
    current_press_zero = current[:]
    target = tuple(map(int, input()))

    impossible = True

    case_not_press_zero = 0
    # 마지막 버튼 누르기 전까지만 확인
    for i in range(1, N - 1):
        if target[i - 1] != current[i - 1]:
            case_not_press_zero += 1
            current[i - 1] ^= 1
            current[i] ^= 1
            current[i + 1] ^= 1
    # 마지막 버튼 체크
    if target[N - 2] != current[N - 2]:
        case_not_press_zero += 1
        current[N - 2] ^= 1
        current[N - 1] ^= 1
    # 마지막 전구 체크
    if target[N - 1] != current[N - 1]:
        case_not_press_zero = 100000
    else:
        impossible = False

    case_press_zero = 1
    current_press_zero[0] ^= 1
    current_press_zero[1] ^= 1
    # 마지막 버튼 누르기 전까지만 확인
    for i in range(1, N - 1):
        if target[i - 1] != current_press_zero[i - 1]:
            case_press_zero += 1
            current_press_zero[i - 1] ^= 1
            current_press_zero[i] ^= 1
            current_press_zero[i + 1] ^= 1
    # 마지막 버튼 체크
    if target[N - 2] != current_press_zero[N - 2]:
        case_press_zero += 1
        current_press_zero[N - 2] ^= 1
        current_press_zero[N - 1] ^= 1
    # 마지막 전구 체크
    if target[N - 1] != current_press_zero[N - 1]:
        case_press_zero = 100000
    else:
        impossible = False

    if impossible:
        print(-1)
        return

    print(min(case_not_press_zero, case_press_zero))


main()


# 보기 좋게 함수화해서 정리한 코드.
"""
import sys
input = sys.stdin.readline

INF = 10**9

def press(arr, i):
    n = len(arr)
    for j in (i-1, i, i+1):
        if 0 <= j < n:
            arr[j] ^= 1

def solve(start, target):
    n = len(start)
    a = start[:]  # 복사
    cnt = 0

    for i in range(1, n):
        if a[i-1] != target[i-1]:
            press(a, i)
            cnt += 1

    if a == target:
        return cnt
    return INF

def main():
    N = int(input().strip())
    start = list(map(int, input().strip()))
    target = list(map(int, input().strip()))

    # 1) 0번 스위치 안 누른 경우
    ans1 = solve(start, target)

    # 2) 0번 스위치 누른 경우
    start2 = start[:]
    press(start2, 0)
    ans2 = 1 + solve(start2, target)

    ans = min(ans1, ans2)
    print(-1 if ans >= INF else ans)

main()

"""
