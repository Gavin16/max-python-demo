# 0629 类
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(11, 20)
print(point.x)


# person新类型
class Person:
    def talk(self):
        print("talk")


john = Person()
john.talk()


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

