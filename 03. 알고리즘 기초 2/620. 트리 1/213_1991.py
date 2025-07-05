'''
문제
이진 트리를 입력받아
전위 순회(preorder traversal), 중위 순회(inorder traversal),
후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1 
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1 
ABDCEFG
DBAECFG
DBEGFCA
'''
# 트리구나! 반갑다.
# 굳이 클래스를 생성해서 트리를 만드는 이유는,
# 그래야 전위, 중위, 후위 순회를 쉽게 돌릴 수 있기 때문이다.

# Node 클래스는 노드 하나를 찍어내는 쿠키틀 역할을 한다.
# 각 Node 객체는 값(value), 왼쪽 자식(left), 오른쪽 자식(right)을 가진다.
class Node: # Node(value)로 사용한다.   
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 트리 구성용 딕셔너리
tree = {} # A : Node(A) 형태로 저장된다.

N = int(input())
for _ in range(N):
    root, left, right = input().split()

    # 딕셔너리는 dict[key] = value의 형태로 쌍을 추가한다.
    if root not in tree: # 중복으로 만들어지지 않게 관리.
        tree[root] = Node(root) # value, left, right가 모두 담긴 객체

    parent = tree[root]
    
    # 트리 특성상 root에서 중복이 제거되면 left, right에는 중복될 일이 없음
    if left != '.':
        tree[left] = Node(left)
        parent.left = tree[left] # Node(root)에 Node(left) 추가
    if right != '.':
        tree[right] = Node(right)
        parent.right = tree[right] # Node(root)에 Node(right) 추가

# 전위 순회: 자신->좌->우 그냥 일반적인 dfs느낌
def preorder(node):
    if node: # None이 아닌 경우
        print(node.value, end='') # 현재노드. 자신을 출력하고
        preorder(node.left) # 자기 왼쪽자식으로 순회하고
        preorder(node.right) # 자기 오른쪽자식으로 순회한다.

# 중위 순회: 좌->자신->우 왼쪽 깊은곳부터 꺼내는 느낌
def inorder(node):
    if node:
        inorder(node.left) # 일단 자기 왼쪽자식으로 순회하고
        print(node.value, end='') # 더이상 왼쪽이 없으면 자신 출력 시작
        inorder(node.right) # 이후 오른쪽 자식을 순회
        
# 후위 순회: 좌->우->자신. 가장 깊은곳부터 꺼내는 느낌
def postorder(node):
    if node:
        postorder(node.left) # 일단 자기 왼쪽자식을 순회하고
        postorder(node.right) # 오른쪽자식으로도 순회하고
        print(node.value, end='') # 리프(자식없음)이 되면 자신 출력 시작

root = tree['A'] # A가 루트다.
preorder(root)
print()
inorder(root)
print()
postorder(root)
