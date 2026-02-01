# Authored by : marigold2003
# Date : 2026-02-01
# Link : https://www.acmicpc.net/problem/3019

import sys

input = sys.stdin.readline


# [Summary]

# 테트리스 블럭을 바닥에 딱 맞춰서 놓는 문제.
# 절대로 블럭과 바닥 사이에 틈이 생겨서는 안 된다.
# 블럭은 회전이 가능하다. 블럭을 놓는 경우의 수를 구하여라.


def main():

    # [Ideas]

    # 이건 딱봐도 구현이다.
    # 필드가 100열까지밖에 안된다. 전부 확인하면 된다.

    ##########

    # 테트리스 블럭 정보
    # 각 블럭마다 열 길이, 바닥에 더할 높이 정보로 저장
    tetris_block_informations = (
        (),
        ((1, (0,)), (4, (0, 0, 0, 0))),
        ((2, (0, 0)),),
        ((3, (0, 0, -1)), (2, (-1, 0))),
        ((3, (-1, 0, 0)), (2, (0, -1))),
        ((3, (0, 0, 0)), (2, (0, -1)), (2, (-1, 0)), (3, (-1, 0, -1))),
        ((3, (0, 0, 0)), (2, (0, 0)), (2, (-2, 0)), (3, (0, -1, -1))),
        ((3, (0, 0, 0)), (2, (0, 0)), (2, (0, -2)), (3, (-1, -1, 0))),
    )

    # C열 필드, P번 블럭
    C, P = map(int, input().split())
    field = tuple(map(int, input().split()))

    count = 0
    # 블럭 정보 가져오기
    for block_len, drs in tetris_block_informations[P]:
        # 전체 필드 확인
        for i in range(C - block_len + 1):
            # 블럭이 놓였을 때 놓인 부분이 평평해지는지 확인
            # 블럭의 높이 정보를 바닥의 높이 정보와 더했을 때 모두 같아지면 참이다.
            if len(set(a + b for a, b in zip(field[i : i + block_len], drs))) == 1:
                count += 1

    print(count)

    ##########

    return


# [Review]

# 발상이 쉬웠다.
# 구현을 어떤 식으로 해야 편할지 생각해보게 되는 문제.
# 원소가 하나인 튜플에는 꼭 콤마를 찍어주자.

if __name__ == "__main__":
    main()
