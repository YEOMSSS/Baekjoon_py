import sys

sys.stdin = open(
    r"C:\Users\junha\OneDrive\Desktop\Baekjoon_py\00. Data Structure\input.txt",
    "r",
)
input = sys.stdin.readline

# -------------------------------
# 여기부터 제출 코드


# Authored by : marigold2003
# Date : 2026-03-15
# Problem Number : 1206


# [Summary] 1206. [S/W 문제해결 기본] 1일차 - View

# 수직선 위에 N(<= 1K)개의 빌딩들이 딱 붙어 있다.
# 각 층(세대)에서 왼쪽과 오른쪽으로 창문을 열었을 때
# 양쪽 모두 2 이상의 공간이 확보되면 조망권이 있다고 표현한다.
# 조망권이 확보된 세대의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 각 빌딩마다 앞뒤 2칸씩 검사해서 세자.
    # 문제에서 이미 padding해서 줬으므로
    # idx 2인 건물부터 확인하면 되겠다. ~N-3 idx

    # 우선 가장 큰 빌딩이 자신이어야 하며
    # 두번째로 큰 빌딩의 높이를 자신의 높이에서 빼면 되겠다.

    ##########

    for tc in range(1, 11):
        # 건물의 수
        N = int(input())
        buildings = list(map(int, input().split()))

        answer = 0
        for i in range(2, N - 2):
            curr = buildings[i]
            candidates = []

            # 이웃 빌딩과 자신의 높이 차이를 저장
            candidates.append(curr - buildings[i - 2])
            candidates.append(curr - buildings[i - 1])
            candidates.append(curr - buildings[i + 1])
            candidates.append(curr - buildings[i + 2])

            count = min(candidates)
            # 높이 차 중 가장 적은 것이 조망권이 보장되는 세대의 수
            # 음수일 경우, 자신이 최고 높이가 아닌 것이다. 그 경우 세대의 수는 0이 된다.
            answer += count if count >= 0 else 0

        print(f"#{tc} {answer}")

    ##########

    return


# [Review]

# 좀 더 최적화할 부분이 있어 보인다.
# 굳이 candidate list를 사용할 필요가 없어 보인다.
# 하드코딩을 더 하면 된다.


if __name__ == "__main__":
    main()
