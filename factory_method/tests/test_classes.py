from unittest.mock import patch

import pytest

from ..classes import (
    ShippingCompany,
    FedEx,
    DHL,
    ShippingCompanyFactory,
)


def test_create_shipping_company_instance():
    with pytest.raises(TypeError) as exc:
        ShippingCompany()

    assert str(exc.value) == (
        "Can't instantiate abstract class ShippingCompany with abstract "
        "methods deliver"
    )


def test_fedex_class():
    assert issubclass(FedEx, ShippingCompany)


def test_dhl_class():
    assert issubclass(DHL, ShippingCompany)


@patch("builtins.print")
def test_fedex_deliver_by_aircraft(print_mock, fedex):
    fedex.deliver_by_aircraft()

    print_mock.assert_called_once_with(
        "FedEx delivered the package by aircraft."
    )


@patch("factory_method.classes.FedEx.deliver_by_aircraft")
def test_fedex_deliver(deliver_by_aircraft_mock, fedex):
    fedex.deliver()

    deliver_by_aircraft_mock.assert_called_once_with()


@patch("builtins.print")
def test_dhl_deliver_by_truck(print_mock, dhl):
    dhl.deliver_by_truck()

    print_mock.assert_called_once_with(
        f"DHL delivered the package by truck."
    )


@patch("factory_method.classes.DHL.deliver_by_truck")
def test_dhl_deliver(deliver_by_truck_mock, dhl):
    dhl.deliver()

    deliver_by_truck_mock.assert_called_once_with()


def test_create_shipping_company_factory_instance():
    with pytest.raises(TypeError) as exc:
        ShippingCompanyFactory()

    assert str(exc.value) == (
        "Can't instantiate abstract class ShippingCompanyFactory with "
        "abstract methods create"
    )


def test_fedex_factory_create(fedex_factory):
    fedex = fedex_factory.create()
    assert isinstance(fedex, FedEx)


def test_dhl_factory_create(dhl_factory):
    dhl = dhl_factory.create()
    assert isinstance(dhl, DHL)
