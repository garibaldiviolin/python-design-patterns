from .classes import AnimalFactory


lion = AnimalFactory.create_animal("lion")
lion.roar()

duck = AnimalFactory.create_animal("duck")
duck.quack()
