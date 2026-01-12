import sys

input = sys.stdin.readline

# 입력이 전부 양수이므로, 최대한 많은 칸을 지나가면 된다.
# 이건 직접 그림을 그려보는 편이 좋을듯.

# r이나 c중에 하나만 홀수여도 모든 칸을 지날 수 있다.
# 그냥 ㄹ모양으로 뽑아버리면 된다.

# 둘 다 짝수면 어떡하지? 무조건 한 칸은 못지나가는데, 그걸 어떻게 판정해야하나.
# 모든 칸을 2*2로 나눌 수 있으니까, 그 안에서 ㄱ, ㄴ, ㅁ 중 선택할 수 있다.
# ㄱ, ㄴ일때 비는 칸만 비울 수 있는 한 칸이 된다. 나머지는 전부 ㅁ이 된다.
# 이동 경로를 어떻게 뽑을 건지만 생각해보자.

# ㄱ ㅁ     ㅁ ㄴ
# ㅁ ㅁ     ㅁ ㅁ   이런 경우는 아래를 큰 ㄷ으로 하면 되고.

# ㅁ ㅁ ㅁ
# ㅁ ㄱ ㅁ
# ㅁ ㅁ ㅁ 위를 뒤집어진 큰 ㄷ으로, 중간은 따로 처리하고, 아래는 큰 ㄷ으로.

# R R  R R  R D
# D L  L L  L L     위행
# D R  R D  R D
# R U    R  U R(D)     ㄱ 3행2열 비우는경우
# D L  L L  L L
# R R  R R  R X     아래행


# ㄱ행 위는     RR...RRDLL...LLD 반복

# ㄱ행 왼쪽은   DRUR 반복
# ㄱ은 RDR, ㄴ은 DRR
# ㄱ행 오른쪽은 URDR 반복
# ㄱ행을 전부 처리 후 마지막을 D로 바꿔줘야 내려갈 수 있다.

# ㄱ행 아래는   LL...LLDRR...RRD 반복, 마지막엔 D없이 끝


def main() -> None:
    R, C = map(int, input().split())
    arr = tuple(tuple(map(int, input().split())) for _ in range(R))

    # 행이 홀수개일때 ㄹ자로 이동
    # 오른쪽~ 아래, 왼쪽~ 아래, 반복 후 오른쪽~ 도착
    if R % 2:
        print(("R" * (C - 1) + "D" + "L" * (C - 1) + "D") * (R // 2) + "R" * (C - 1))
        return

    # 열이 홀수개일때 N자로 이동
    # 아래~ 오른쪽, 위~ 오른쪽, 반복 후 아래~ 도착
    if C % 2:
        print(("D" * (R - 1) + "R" + "U" * (R - 1) + "R") * (C // 2) + "D" * (R - 1))
        return

    # 행과 열이 모두 짝수일 경우 2*2로 나눈 칸의 우상과 좌하칸은 비워질 수 있는 칸들이다.
    # 전부 비교해서 가장 작은 값을 비우고 나머지를 전부 순회한다.
    min_coord = (0, 0)
    min_value = sys.maxsize
    for r in range(0, R, 2):

        for c in range(1, C, 2):
            temp = arr[r][c]
            if temp < min_value:
                min_value = temp
                min_coord = (r, c)

        for c in range(0, C, 2):
            temp = arr[r + 1][c]
            if temp < min_value:
                min_value = temp
                min_coord = (r + 1, c)

    # 2*2칸씩 묶었을 때의 좌표
    pos = (min_coord[0] // 2, min_coord[1] // 2)

    # 최소값 행의 위쪽 행은 반전된 ㄷ자
    upper = ("R" * (C - 1) + "D" + "L" * (C - 1) + "D") * pos[0]

    # 최소값 행에서 왼쪽은 u자
    left = "DRUR" * pos[1]
    # 최소값의 좌표 행이 짝수면 ㄴ, 홀수면 ㄱ
    center = "RDR" if min_coord[0] % 2 else "DRR"
    # 최소값 행에서 오른쪽은 n자
    right = "URDR" * (C // 2 - 1 - pos[1])
    middle = left + center + right

    # 최소값 행의 아래쪽 행은 ㄷ자
    lower = ("L" * (C - 1) + "D" + "R" * (C - 1) + "D") * (R // 2 - 1 - pos[0])

    result = upper + middle[:-1] + "D" + lower
    # 마지막(도착지)은 출력하지 않는다.
    print(result[:-1])


if __name__ == "__main__":
    main()
