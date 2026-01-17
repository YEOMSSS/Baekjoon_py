"""
문제
이진트리를 다음의 규칙에 따라 행과 열에 번호가 붙어있는 격자 모양의 틀 속에 그리려고 한다.
이때 다음의 규칙에 따라 그리려고 한다.

이진트리에서 같은 레벨(level)에 있는 노드는 같은 행에 위치한다.
한 열에는 한 노드만 존재한다.
임의의 노드의 왼쪽 부트리(left subtree)에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고,
오른쪽 부트리(right subtree)에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.
노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.
이와 같은 규칙에 따라 이진트리를 그릴 때 각 레벨의 너비는
그 레벨에 할당된 노드 중 가장 오른쪽에 위치한 노드의 열 번호에서
가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다.
트리의 레벨은 가장 위쪽에 있는 루트 노드가 1이고 아래로 1씩 증가한다.

아래 그림은 어떤 이진트리를 위의 규칙에 따라 그려 본 것이다.
첫 번째 레벨의 너비는 1, 두 번째 레벨의 너비는 13, 3번째, 4번째 레벨의 너비는 각각 18이고,
5번째 레벨의 너비는 13이며, 그리고 6번째 레벨의 너비는 12이다.

우리는 주어진 이진트리를 위의 규칙에 따라 그릴 때에 너비가 가장 넓은 레벨과 그 레벨의 너비를 계산하려고 한다.
위의 그림의 예에서 너비가 가장 넓은 레벨은 3번째와 4번째로 그 너비는 18이다.
너비가 가장 넓은 레벨이 두 개 이상 있을 때는 번호가 작은 레벨을 답으로 한다.
그러므로 이 예에 대한 답은 레벨은 3이고, 너비는 18이다.

임의의 이진트리가 입력으로 주어질 때 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 프로그램을 작성하시오

입력
첫째 줄에 노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)이 주어진다.
다음 N개의 줄에는 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호가 순서대로 주어진다.
노드들의 번호는 1부터 N까지이며, 자식이 없는 경우에는 자식 노드의 번호에 -1이 주어진다.

출력
첫째 줄에 너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력한다.
너비가 가장 넓은 레벨이 두 개 이상 있을 때에는 번호가 작은 레벨을 출력한다.

예제 입력 1
19
1 2 3
2 4 5
3 6 7
4 8 -1
5 9 10
6 11 12
7 13 -1
8 -1 -1
9 14 15
10 -1 -1
11 16 -1
12 -1 -1
13 17 -1
14 -1 -1
15 18 -1
16 -1 -1
17 -1 19
18 -1 -1
19 -1 -1
예제 출력 1
3 18
"""

# 재밌긴했다. 진짜로. 중위순회dfs, 루트찾기, depth찾기, Class로 트리만들기..
# 복잡하다 복잡해


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 루트 탐색용
all_nodes = set()
child_nodes = set()

tree = {}
N = int(input())
for _ in range(N):
    root, left, right = map(int, input().split())

    all_nodes.add(root)
    if root not in tree:
        tree[root] = Node(root)

    parent = tree[root]

    if left != -1:
        child_nodes.add(left)
        if left not in tree:  # 초기화 방지.
            tree[left] = Node(left)
        parent.left = tree[left]

    if right != -1:
        child_nodes.add(right)
        if right not in tree:
            tree[right] = Node(right)
        parent.right = tree[right]

# 중위순회하면 문제에서 요구하는대로 순회할 수 있다.
from collections import defaultdict

# defaultdict(list)는 key를 생성할 때 무조건 빈 리스트로 만든다. 쌩으로 append가능
level = defaultdict(list)  # level[depth]에 order를 저장한다.
order = 0  # 중위순회한 순서


# 중위순회 dfsR
def inorder(node, depth):
    global order
    if node:
        inorder(node.left, depth + 1)
        order += 1  # append될 때 순서는 1씩 늘려준다.
        level[depth].append(order)
        inorder(node.right, depth + 1)


# 부모가 없는 노드가 루트가 된다.
root = (all_nodes - child_nodes).pop()
inorder(tree[root], 1)

answer = [0] * (len(level) + 1)
# 딕셔너리에 .items()를 꼭 붙여 튜플로 바꿔줘야 value까지 반환된다.
for key, value in level.items():
    width = max(value) - min(value) + 1  # 레벨에서 가장 긴 너비구하기
    answer[key] = width  # answer[level]에 너비를 저장

max_answer = max(answer)  # 가장 긴 너비 뽑기.
print(answer.index(max_answer), max_answer)  # 동일너비면 낮은레벨 인덱스.

# 어흐 씨빨씨발씨빨
