class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


head = None


def addNode(who):
    global head

    newNode = Node(who)
    if not head:
        head = newNode
    else:
        # head밖에 모르니까 where를 이동시켜 끝 노드로 이동한다.
        where = head
        while where.link:
            where = where.link
        # 마지막 노드에 연결해주기
        where.link = newNode

        # 근데 이럴거면, 그냥 tail도 global로 하면 연결이 훨씬 편하지 않나.

    return newNode


def deleteNode(before: Node):
    before.link = before.link.link
    return before.link


for i in range(1, 42):
    tail = addNode(i)
tail.link = head


where = head
# 내 다음다음사람이 나라면 둘만 남은 것이다. (또는 하나긴 한데, 한명씩 짤리니까)
while where.link.link != where:
    where = where.link
    deleteNode(where)

print(where.data)
print(where.link.data)
