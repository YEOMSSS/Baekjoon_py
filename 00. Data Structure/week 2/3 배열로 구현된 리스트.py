capacity = 5
array = [None] * capacity
size = 0


# arr이 비어있으면 True return
def isEmpty():
    if size == 0:
        return True
    else:
        return False


# arr이 가득 차있으면 True return
def isFull():
    return size == capacity


# pos가 올바를 때 arr[pos] return
def getEntry(pos):
    if 0 <= pos < size:
        return array[pos]
    else:
        return None


# arr[pos]에 e를 삽입
# 만약 중간에 삽입될 경우, 뒤로 밀고 삽입
def insert(pos, e):
    global size
    if size < capacity and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i - 1]
        array[pos] = e
        size += 1


# pos가 올바를 때 뒤를 앞으로 당겨와서 삭제
def delete(pos):
    global size
    if size > 0 and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i + 1]
        size -= 1
        return e


if __name__ == "__main__":
    # 최초는 None으로 이루어져 빈 리스트[]가 출력된다.
    print("최초   ", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5 ", array[0:size])
    delete(2)
    print("삭제(2)", array[0:size])
    # print(array)
    delete(size - 1)
    print("삭제(E)", array[0:size])
    # print(array)
    delete(0)
    print("삭제(0)", array[0:size])
    # print(array)
