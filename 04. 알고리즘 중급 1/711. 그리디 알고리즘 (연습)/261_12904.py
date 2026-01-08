import sys

input = sys.stdin.readline

# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.
# 이 두 가지 방법만 이용해서 S를 T로 만들어라.

# 거꾸로 가보자. T의 맨 끝이 A면 pop한다.
# B면 pop하고 뒤집는다.


from collections import deque


def main() -> None:
    S = deque(input().rstrip())
    S_len = len(S)
    T = deque(input().rstrip())
    T_len = len(T)

    # 뒤집힘 처리용
    reverse_flag = False

    while T:

        if S_len == T_len:
            if reverse_flag:
                S.reverse()

            if S == T:
                print(1)
                return

        # 뒤집힌 상태가 아닐 경우 pop
        if not reverse_flag:
            if T[-1] == "B":
                reverse_flag = True
            T.pop()

        # 뒤집힌 경우 0이 B면 popleft
        else:
            if T[0] == "B":
                reverse_flag = False
            T.popleft()

        T_len -= 1

    print(0)


if __name__ == "__main__":
    main()
