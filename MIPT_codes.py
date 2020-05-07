def f(n:int):
    """factorial"""
    assert n >= 0, "factorial not defined"
    if n == 0:
        return 1
    return f(n-1)*n

def gcd(a,b):
    """Evclid algorithm - наибольший общий делитель"""
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

def gcd2(a,b):
    """Evclid algorithm #2 - наибольший общий делитель"""
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def gcd3(a,b):
    return a if b == 0 else gcd(b, a%b)

def pow (a, n)
    """быстрое возведение в степень целых чисел"""
    assert a > 0
    if n == 0:
        return 1
    elif: #для n нечетные
        return pow(n-1)*a
    else: #для n четные
        return pow(n**2, n//2)

def traj_num (N):
    """загадко про количество прыжков кузнечика с типами шагов 1, 2"""
    K = [0, 1] + [0] * N
    for i in range (2, N+1):
        K[i] = K[i-2] + K[i-1]
    return K[N]

def count_traj (N, allowed:list):
    """загадко про количество прыжков кузнечика с запрещенными точками 4 и 7 и типами шагов 1, 2, 3"""
    K = [0, 1, int(allowed[2])] + [0] * (N-3)
    for i in range (3, N+1):
        if allowed[i]:
            K[i] = K[i-3] + K[i - 2] + K[i - 1]
    return K[N]

#ОБЪЕКТЫ И КЛАССЫ
class Goat: # объявление класса
    """Объекты и классы на примере козы ))))"""
    legs_number = 4 #общий атрибут объектов класса при изменении значения отрибута, он изменится для всех переменных класса
    def __init__(self, height, weight): #объявление методов объектов класса
        self.height = height
        self.weight = weight
    def __str__(self): #объявление возможности печати методов
        s = "weight = {}, height = {}".format(self.height, self.weight)
        return s
#примеры создания
marusya = Goat(60, 40)
notka = Goat(50, 30)
#вывод методов
for x in notka, marusya:
    print (x)
#изменение значений методов
notka.weight += 1
x = notka
x.weight += 5

#ИМЕНОВАННЫЕ КОРТЕЖИ
A = (1, 2, 3)
r = math.sqtt(A[0]**2, A[1]**2, A[2]**2) #неудобно
from collections import namedtuple:
Point = namedtuple("Point", "x y z") #имя типа или класса - с большой буквы
A = Point(1, 0,3)
print(A.x)

#СВЯЗАННЫЙ СПИСОК
a = [1]
a.append([2])
a[1].append([3, a]) #закольцевали список
a[1].append([3, None]) #корректный пример
p = a
while p is not None:
    print(p[0])
    p = p[1]

class Linked_list:
    def __init__(self):
        self._begin = None
    def insert(self, x):
        self._begin = [x, self._begin]
    def pop(self):
        assert self._begin is not None, "list empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x