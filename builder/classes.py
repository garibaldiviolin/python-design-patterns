from abc import ABC, abstractmethod


class House:
    pass


class HouseBuilder(ABC):

    @abstractmethod
    def start_house(self):
        pass

    @abstractmethod
    def add_bathroom(self):
        pass

    @abstractmethod
    def add_bedroom(self):
        pass

    @abstractmethod
    def built_house(self):
        pass


class ConcreteHouseBuilder(ABC):

    def start_house(self):
        self._house = House()

    def add_bedrooms(self, number):
        try:
            self._house.bedrooms += number
        except AttributeError:
            self._house.bedrooms = number

    def add_living_rooms(self, number):
        try:
            self._house.living_rooms += number
        except AttributeError:
            self._house.living_rooms = number

    def add_bathrooms(self, number):
        try:
            self._house.bathrooms += number
        except AttributeError:
            self._house.bathrooms = number

    @property
    def house(self):
        return self._house


class Foreman:
    def __init__(self, house_builder):
        self._house_builder = house_builder

    def build_mansion(self):
        self._house_builder.start_house()
        self._house_builder.add_bedrooms(10)
        self._house_builder.add_bathrooms(10)
        self._house_builder.add_living_rooms(1)
        return self._house_builder.house

    def build_small_house(self):
        self._house_builder.start_house()
        self._house_builder.add_bedrooms(1)
        self._house_builder.add_bathrooms(1)
        return self._house_builder.house
