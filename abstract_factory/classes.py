from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def run(self):  # pragma: no cover
        pass


class Ferrari(Car):
    def run(self):
        print(f"{self.__class__.__name__} is driving very fast!")


class Lamborghini(Car):
    def run(self):
        print(f"{self.__class__.__name__} is at top speed!")


class Aircraft(ABC):

    @abstractmethod
    def fly(self):  # pragma: no cover
        pass


class AirbusA380(Aircraft):
    def fly(self):
        print(f"{self.__class__.__name__} is flying above the clouds!")


class Boeing747(Aircraft):
    def fly(self):
        print(f"{self.__class__.__name__} is very high!")


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self):  # pragma: no cover
        pass

    @abstractmethod
    def create_aircraft(self):  # pragma: no cover
        pass


class ConcreteVehicleFactory1(VehicleFactory):

    @classmethod
    def create_car(cls):
        return Ferrari()

    @classmethod
    def create_aircraft(cls):
        return AirbusA380()


class ConcreteVehicleFactory2(VehicleFactory):

    @classmethod
    def create_car(cls):
        return Lamborghini()

    @classmethod
    def create_aircraft(cls):
        return Boeing747()
