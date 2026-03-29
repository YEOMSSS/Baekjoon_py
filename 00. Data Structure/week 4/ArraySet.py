class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0 : self.size])

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else:
            pass

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])

        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])

        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(setB.size):
            if self.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC


# from ArraySet import ArraySet
if __name__ == "__main__":

    setA = ArraySet()
    setB = ArraySet()

    # 집합 A
    setA.insert(10)
    setA.insert(20)
    setA.insert(30)

    # 집합 B
    setB.insert(20)
    setB.insert(30)
    setB.insert(40)
    setB.insert(50)

    print("집합 A :", setA)
    print("집합 B :", setB)

    # 포함 여부
    print("A에 10 포함?", setA.contains(10))
    print("B에 60 포함?", setB.contains(60))

    # 합집합
    print("A ∪ B :", setA.union(setB))

    # 교집합
    print("A ∩ B :", setA.intersect(setB))

    # 차집합
    print("A - B :", setA.difference(setB))

    # 원소 삭제
    setA.delete(20)
    print("삭제 후 :", setA)
