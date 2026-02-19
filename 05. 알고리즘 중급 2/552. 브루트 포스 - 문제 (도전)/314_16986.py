# Authored by : marigold2003
# Date : 2026-02-18
# Link : https://www.acmicpc.net/problem/16986


import sys

input = sys.stdin.readline


# [Summary] 인싸들의 가위바위보

# 가위불바위총번개악마용물공기보스펀지늑대나무사람뱀 은 가위바위보의 확장판이다.
# 인싸가위바위보를 이와 비슷한 형태로 만들 것이며, 손동작의 종류는 N(9)개이다.
# 손동작의 상성과 상대할 두 사람이 낼 손동작이 입력된다.

# 경기진행순서는 지우, 경희, 민호 순이다.
# 경기진행순서가 더 뒤인 사람이 무승부일 때 승리를 가져간다. 민호 > 경희 > 지우
# 이전 경기의 승자와 이전 경기에 참여하지 않은 사람이 다음 경기를 진행해 또 승자를 결정한다.
# 지우가 모든 손동작을 사용해 N회 경기할 때, 가장 먼저 K(6)번 우승할 수 있을지 판단하시오.


# a 승리(b 패배) False return
# a 패배(b 승리, 무승부) True return
def game(a, b, rcp_info) -> bool:
    result = rcp_info[b][a]
    # b가 패배
    if not result:
        return False
    # b가 승리 or 무승부(b가 승리)
    else:
        return True


def main() -> None:

    # [Ideas]

    # 지우는 경기가 몇 번 진행되던 N회를 넘길 수 없다.
    # 9! = 362880. 브루트포스로 지우의 모든 경우의 수를 만들어 시뮬레이션하자.

    ##########

    N, K = map(int, input().split())
    # [i][j]에서 i가 j를 만났을 때의 승패정보 0패 1비 2승
    rcp_info = tuple(tuple(map(int, input().split())) for _ in range(N))

    kh_play = tuple(map(lambda x: int(x) - 1, input().split()))
    mh_play = tuple(map(lambda x: int(x) - 1, input().split()))

    from itertools import permutations

    hands = [None, kh_play, mh_play]
    # a가 내는 손바닥 순서의 모든 경우의 수
    for jw_play in permutations(range(N)):
        jw, kh, mh = 0, 1, 2
        hands[jw] = jw_play

        count_win = [0] * 3
        count_play = [0] * 3

        winner = jw
        challenger = kh
        loser = mh

        # 승수 달성 시 경기 종료
        while K not in count_win and count_play[0] < N:
            # sort로 정리해서 game에 넣으면 졌을때만 뒤에있는놈이 승리하고
            # 나머지 모든 경우에서 앞에있는놈이 이기게 할 수 있다.

            # 무승부일 때 이기는 사람이 뒤로 가게 정렬
            if winner > challenger:
                winner, challenger = challenger, winner

            # 뒤가 앞을 이기면 True가 return됨
            result = game(
                hands[winner][count_play[winner]],
                hands[challenger][count_play[challenger]],
                rcp_info,
            )

            # 승자, 다음 도전자, 패자(다음 경기 미참여)
            if result:
                winner, challenger, loser = challenger, loser, winner
            else:
                winner, challenger, loser = winner, loser, challenger

            # 승자의 승수 1++
            count_win[winner] += 1

            # 게임 참여자의 손바닥 순서 카운트 1++
            count_play[winner] += 1
            count_play[loser] += 1

        if count_win[0] == K:
            print(1)
            return

    print(0)

    ##########

    return


# [Review]

# 구현하기 재밌는 문제.
# 실수하기 몹시 쉽다. 신경쓸 부분이 많음.


if __name__ == "__main__":
    main()
