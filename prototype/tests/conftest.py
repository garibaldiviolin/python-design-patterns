from prototype.classes import Sheep

import pytest


@pytest.fixture
def sheep():
    return Sheep("Lucky")


@pytest.fixture
def sheep2(sheep):
    return sheep.clone()
