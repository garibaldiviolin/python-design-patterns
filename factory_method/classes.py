from abc import ABC, abstractmethod


class ShippingCompany(ABC):

    @abstractmethod
    def deliver():
        pass


class FedEx(ShippingCompany):
    def deliver_by_aircraft(self):
        print(f"{self.__class__.__name__} delivered the package by aircraft.")

    def deliver(self):
        self.deliver_by_aircraft()


class DHL(ShippingCompany):
    def deliver_by_truck(self):
        print(f"{self.__class__.__name__} delivered the package by truck.")

    def deliver(self):
        self.deliver_by_truck()


class ShippingCompanyFactory(ABC):
    @abstractmethod
    def create():
        pass


class FedExFactory(ShippingCompanyFactory):
    @classmethod
    def create(cls):
        return FedEx()


class DHLFactory(ShippingCompanyFactory):
    @classmethod
    def create(cls):
        return DHL()
