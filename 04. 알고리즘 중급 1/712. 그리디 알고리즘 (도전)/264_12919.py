import sys

input == sys.stdin.readline

# 261_12904와 비슷한 문제. 다만 B에 대한 동작이 바뀐다.

# 문자열의 뒤에 A를 추가한다.
# 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
# 이 두 가지 방법만 이용해서 S를 T로 만들어라.

# A BA BAA BAAB BBAAB BBAABA
# 두 가지 경우가 생긴다.
# 1. 맨앞이 B면 popleft하고 뒤집어 이전단계로 갈 수 있다. BBAABA <- ABAAB
# 2. 맨뒤가 A면 pop해서 이전단계로 갈 수 있다. BBAABA <- BBAAB
# 아씨 어떡하지? bfs를 해볼까?

# 풀고 나니 드는 생각이지만 굳이 거꾸로 갈 필요 없이, S를 T로 만드는 bfs를 돌려도 될 듯.
# 다만 이 경우는 좀 더 로직이 필요할 것 같다. 비용이 좀 드네


from collections import deque


# 그냥 재귀로 돌리는게 나았을라나?
def main_R() -> None:

    S = list(input().rstrip())
    T = list(input().rstrip())

    def dfsR(t) -> None:

        # S와 같아지면 코드 종료
        if t == S:
            print(1)
            sys.exit(0)

        # t가 사라져 버리면 아무 일도 일어나지 않는다.
        if len(t) == 0:
            return

        # t가 A로 끝나면 제거 후 재귀
        if t[-1] == "A":
            dfsR(t[:-1])

        # t가 B로 시작하면 제거 후 뒤집은 후 재귀
        if t[0] == "B":
            dfsR(t[1:][::-1])

    dfsR(T)

    # dfsR이 종료되지 않았다면 도달 불가
    print(0)


def main() -> None:
    S = tuple(input().rstrip())
    S_len = len(S)
    T = tuple(input().rstrip())
    T_len = len(T)

    queue = deque()
    queue.append((0, T_len - 1, False))

    while queue:
        # 최좌측 인덱스, 최우측 인덱스, 뒤집힘 확인용 부울
        left, right, flag = queue.popleft()

        # 길이가 같아지면 비교해본다.
        if right + 1 - left == S_len:

            # flag에 따라 뒤집힘 처리
            if flag:
                temp = T[left : right + 1][::-1]
            else:
                temp = T[left : right + 1]

            # 일치할 경우 코드 종료
            if temp == S:
                print(1)
                return

            # 불일치 시 bfs 계속 진행
            continue

        # 뒤집히지 않은 상태일 때
        if not flag:
            if T[left] == "B":
                queue.append((left + 1, right, not flag))

            if T[right] == "A":
                queue.append((left, right - 1, flag))

        # 뒤집힌 상태일 때
        if flag:
            if T[right] == "B":
                queue.append((left, right - 1, not flag))

            if T[left] == "A":
                queue.append((left + 1, right, flag))

    print(0)


if __name__ == "__main__":
    main_R()
