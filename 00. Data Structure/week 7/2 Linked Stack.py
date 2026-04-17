# 일단 붕어빵 틀부터
class newNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


top = None


def isEmpty():
    return top is None


def push(elem):
    global top
    # n = newNode(elem)
    # n.link = top
    # top = n
    top = newNode(elem, top)


def pop():
    global top
    if isEmpty():
        print("스택 비어있음")
        exit()

    value = top.data
    top = top.link
    return value


# top의 data 확인
def peek():
    if isEmpty():
        return None
    return top.data


def size():
    count = 0
    where = top
    while where:
        count += 1
        where = where.link
    return count


def display():
    where = top
    result = []

    while where:
        result.append(where.data)
        where = where.link
    print(result)


push(10)
push(20)
push(30)
display()
print(size())

print(pop())
display()
print(peek())
