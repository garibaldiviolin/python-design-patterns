from ..classes import (
    Ferrari,
    Lamborghini,
    AirbusA380,
    Boeing747,
)

import pytest


@pytest.fixture
def ferrari():
    return Ferrari()


@pytest.fixture
def lamborghini():
    return Lamborghini()


@pytest.fixture
def airbus_a380():
    return AirbusA380()


@pytest.fixture
def boeing_747():
    return Boeing747()
