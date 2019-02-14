class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part

MyBuf = Buffer()
MyBuf.add(1, 2, 3)
print(MyBuf.get_current_part()) # вернуть [1, 2, 3]
MyBuf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(MyBuf.get_current_part()) # вернуть [6]
MyBuf.add(7, 8, 9, 10) # 40
print(MyBuf.get_current_part()) # []
MyBuf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # 5 5
print(MyBuf.get_current_part()) # 1