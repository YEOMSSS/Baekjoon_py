import sys

input = sys.stdin.readline

# 중위순회 inorder와 후위순회 postorder가 주어질 때 전위순회 preorder 찾기
# 최대 10만노드까지 들어올 수 있기 때문에 브루트포스가 되면
# 카탈란 수 10만 = 3 * 10**18만 지랄났네.

# 후위 1 3 2일때 5가지 형태가 생긴다.

#     2   2   2   2   2
#    /   /   / \   \   \
#   3   3   1   3   3   3
#  /     \         /     \
# 1       1       1       1

# 후위순회의 마지막 노드가 루트임은 자명하다.

# 전위순회는 루트->좌서브트리->우서브트리 순서로 순회

# 중위순회는 좌서브트리->루트->우서브트리 순서로 순회
# 후위순회는 좌서브트리->우서브트리->루트 순서로 순회

# 중위순회에서 루트를 떼면 트리가 좌우로 나눠진다.
# 중위순회로 각 서브트리의 길이를 알 수 있다.

# 그럼 후위순회에서 각 서브트리의 루트를 알 수 있다.
# 후위순회는 좌측우측루트의 묶음으로 이루어져있으므로,
# 좌측의 길이를 구해 떼주고 현재루트를 떼주면 우측이 된다.

# 재귀문제는 python으로.
sys.setrecursionlimit(300000)


def main() -> None:
    N = int(input())

    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    # inorder 인덱스 맵
    pos = {val: idx for idx, val in enumerate(inorder)}

    # 분할정복으로 재귀하여 루트를 찾아 나가자.
    def solve_R(in_l: int, in_r: int, post_l: int, post_r: int) -> None:

        # 서브트리의 길이가 0이 되면 종료
        if in_l > in_r:
            return

        # 현재 서브트리의 루트 찾기
        root = postorder[post_r]
        root_idx = pos[root]

        # 전위순회는 루트->좌서브->우서브
        print(root, end=" ")

        # 좌서브트리 크기 = 중위순회 루트인덱스 - 중위순회 시작인덱스
        left_size = root_idx - in_l

        # 좌서브트리의 루트를 찾기 위해 재귀
        # inorder는 시작 ~ 루트전, postorder는 시작 ~ 좌서브트리끝
        solve_R(in_l, root_idx - 1, post_l, post_l + left_size - 1)

        # 우서브트리의 루트를 찾기 위해 재귀
        # inorder는 루트후 ~ 끝, postorder는 좌서브트리직후 ~ 끝-1 (루트제거)
        solve_R(root_idx + 1, in_r, post_l + left_size, post_r - 1)

    solve_R(0, N - 1, 0, N - 1)


if __name__ == "__main__":
    main()
