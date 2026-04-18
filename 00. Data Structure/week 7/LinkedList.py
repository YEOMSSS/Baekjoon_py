# Linked List.
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next


# 코드 6.5: 연결리스트 클래스
class LinkedList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__(self):
        self.head = None

    # 리스트의 연산: 클래스의 메소드
    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False

    def getNode(self, where):
        if where < 0:
            return None
        node = self.head
        while where > 0 and node != None:
            node = node.link
            where -= 1
        return node

    def getEntry(self, where):
        node = self.getNode(where)
        if node == None:
            return None
        else:
            return node.data

    def __str__(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.data)
            node = node.link
        return str(result)

    def insert(self, where, elem):
        before = self.getNode(where - 1)
        if before == None:  # 맨 앞에 삽입함
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, where):
        before = self.getNode(where - 1)
        if before == None:  # 맨 앞 노드를 삭제
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


# ===============
if __name__ == "__main__":
    L = LinkedList()

    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)
