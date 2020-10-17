from factory_method.classes import FedExFactory, DHLFactory, FedEx, DHL

import pytest


@pytest.fixture
def fedex():
    return FedEx()


@pytest.fixture
def dhl():
    return DHL()


@pytest.fixture
def fedex_factory():
    return FedExFactory()


@pytest.fixture
def dhl_factory():
    return DHLFactory()
