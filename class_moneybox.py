class MoneyBox:
    #конструктор с аргументом – вместимость копилки
    def __init__(self, capacity=0, how_much_money_is_keeping=0):
        self.capacity = capacity
        self.how_much_money_is_keeping = how_much_money_is_keeping

    # True, если можно добавить v монет, False иначе
    def can_add(self, v):
        if v <= self.capacity:
            return True
        return False

    # положить v монет в копилку
    def add(self, v):
        self.how_much_money_is_keeping += v
        self.capacity -= v

MyBox = MoneyBox(10)
print(MyBox.capacity)
MyBox.add(8)
print(MyBox.how_much_money_is_keeping)
print(MyBox.capacity)
print(MyBox.can_add(2))
MyBox.add(2)
print(MyBox.capacity)



