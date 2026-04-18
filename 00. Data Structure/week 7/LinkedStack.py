# 코드 6.1: 단순연결노드 클래스
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


# 코드 6.2: 연결된 스택 클래스
class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, item):
        self.top = Node(item, self.top)

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    # 코드 6.3: 연결된 스택의 전체 요소의 수 계산
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1

    # 코드 6.4: 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)


# ===========================
if __name__ == "__main__":
    s = LinkedStack()  # 스택 객체를 생성

    s.push("A")
    s.push("B")
    s.push("C")

    while not s.isEmpty():
        print(s.pop(), end=" ")
