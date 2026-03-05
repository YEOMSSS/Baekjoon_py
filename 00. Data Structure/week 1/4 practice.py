start, end = 3, 6
Data = [1, 2, 3, 4, 5, 6]
dummy = Data[3:6]
dummy.reverse()
Data[3:6] = dummy
print(Data)
