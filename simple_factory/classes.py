class Duck():
    def quack(self):
        print("Quack quack...")


class Lion:
    def roar(self):
        print("Roaring...")


class AnimalFactory:
    cataloged_species = {
        "duck": Duck,
        "lion": Lion,
    }

    @classmethod
    def create_animal(cls, species):
        species_class = cls.cataloged_species[species]
        return species_class()
