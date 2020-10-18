from unittest.mock import patch

import pytest

from ..classes import (
    Car,
    Ferrari,
    Lamborghini,
    Aircraft,
    AirbusA380,
    Boeing747,
    VehicleFactory,
    ConcreteVehicleFactory1,
    ConcreteVehicleFactory2,
)


def test_create_car_instance():
    with pytest.raises(TypeError) as exc:
        Car()

    assert str(exc.value) == (
        "Can't instantiate abstract class Car with abstract methods run"
    )


def test_ferrari_class():
    assert issubclass(Ferrari, Car)


@patch("builtins.print")
def test_ferrari_run(print_mock, ferrari):
    ferrari.run()

    print_mock.assert_called_once_with("Ferrari is driving very fast!")


def test_lamborghini_class():
    assert issubclass(Lamborghini, Car)


@patch("builtins.print")
def test_lamborghini_run(print_mock, lamborghini):
    lamborghini.run()

    print_mock.assert_called_once_with("Lamborghini is at top speed!")


def test_create_aircraft_instance():
    with pytest.raises(TypeError) as exc:
        Aircraft()

    assert str(exc.value) == (
        "Can't instantiate abstract class Aircraft with abstract methods fly"
    )


def test_airbus_a380_class():
    assert issubclass(AirbusA380, Aircraft)


@patch("builtins.print")
def test_airbus_a380_run(print_mock, airbus_a380):
    airbus_a380.fly()

    print_mock.assert_called_once_with(
        "AirbusA380 is flying above the clouds!"
    )


def test_boeing_747_class():
    assert issubclass(Boeing747, Aircraft)


@patch("builtins.print")
def test_boeing_747_run(print_mock, boeing_747):
    boeing_747.fly()

    print_mock.assert_called_once_with("Boeing747 is very high!")


def test_create_abstract_vehicle_factory_instance():
    with pytest.raises(TypeError) as exc:
        VehicleFactory()

    assert str(exc.value) == (
        "Can't instantiate abstract class VehicleFactory with abstract "
        "methods create_aircraft, create_car"
    )


def test_vehicle_factory1_class():
    assert issubclass(ConcreteVehicleFactory1, VehicleFactory)


def test_vehicle_factory1_create_car():
    car = ConcreteVehicleFactory1.create_car()
    assert isinstance(car, Ferrari) is True


def test_vehicle_factory1_create_aircraft():
    aircraft = ConcreteVehicleFactory1.create_aircraft()
    assert isinstance(aircraft, AirbusA380) is True


def test_vehicle_factory2_class():
    assert issubclass(ConcreteVehicleFactory2, VehicleFactory)


def test_vehicle_factory2_create_car():
    car = ConcreteVehicleFactory2.create_car()
    assert isinstance(car, Lamborghini) is True


def test_vehicle_factory2_create_aircraft():
    aircraft = ConcreteVehicleFactory2.create_aircraft()
    assert isinstance(aircraft, Boeing747) is True
