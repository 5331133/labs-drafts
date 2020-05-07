class MoneyBox():
    def __init__(self, capacity):
        """конструктор с аргументом – вместимость копилки"""
        self.capacity = capacity
        self.v = 0

    def can_add(self, v):
        """True, если можно добавить v монет, False иначе"""
        print (self.capacity, (self.capacity - v) > 0, self.capacity - v)
        return (self.capacity - v) >= 0

    def add(self, v):
        """положить v монет в копилку"""
        if self.can_add(v) is True:
            print ('before', v, self.capacity)
            self.capacity -= v
            print ('after', v, self.capacity)
        else: print (self.capacity)


#x = MoneyBox(int(input('capacity = ')))
x = MoneyBox(11)
x.add(5)
x.add(1)
x.add(4)
x.add(3)
x.add(7)

