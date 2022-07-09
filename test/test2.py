class Dog():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = '0'

    def sit(self):
        print(self.c.title())

    def roll(self):
        print(self.a.title())


dog = Dog('w', '6')


class Dogg(Dog):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.z = 'Z'
    def describ(self):
        print("wwwww"+self.z)


dogg = Dogg('a', 'b')

dog.a = 'z'
print(dog.c.title())
dog.roll()
print(dogg.a.title())
dogg.describ()
dogg.roll()