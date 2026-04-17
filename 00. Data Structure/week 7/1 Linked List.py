class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


# 투룸을 찍어낸다.
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# 링크방을 이용해 서로 연결해준다.
node1.link = node2
node2.link = node3
node3.link = node4
node4.link = node5

# 시작 노드를 기록해둔다.
where = node1

# print(node1.data)
# print(where.data)

while where:
    print(where.data)
    where = where.link
