import sys

input = sys.stdin.readline


# 버블정렬에서 실제로 발생하는 스왑 횟수 = 배열의 인버전 개수
# 그렇다면 머지소트를 하되, 인버전의 개수만 빠르게 세자.


def main():
    N = int(input())
    arr = list(map(int, input().split()))

    # 절반으로 계속 나눠서 정렬하고 합치고를 반복한다.
    def solve_R(start, end):

        # 배열길이가 0~1이면 이미 정렬된 상태
        # 배열길이가 0이 될 일은 없긴 하다.
        if end - start == 1:
            return 0

        mid = (start + end) // 2

        # left 내부 정렬 비용 + right 내부 정렬 비용
        count = solve_R(start, mid) + solve_R(mid, end)

        temp = []
        left, right = start, mid

        # left나 right중 하나를 전부 확인할 때까지 반복
        while left < mid and right < end:

            # 정순일 때 그대로
            if arr[left] <= arr[right]:
                # 스왑이 없으니, 더 작은 left를 그대로 append
                temp.append(arr[left])
                left += 1

            # 역순일 때 left까지 mid-left회 스왑
            else:
                # mid-left회 스왑해서 앞으로 이동한 right를 append
                temp.append(arr[right])
                count += mid - left
                right += 1

        # 남은 정렬된 값들 추가, 당연히 left부터 확인
        temp.extend(arr[left:mid])
        temp.extend(arr[right:end])

        # 한 턴 정렬된 값으로 갱신
        arr[start:end] = temp

        # left + right를 정렬하는데 든 비용
        return count

    print(solve_R(0, N))


if __name__ == "__main__":
    main()
