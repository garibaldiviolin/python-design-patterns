class Sheep:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f'{self.name}: "Baa..."')

    def clone(self):
        return self.__class__(self.name)
