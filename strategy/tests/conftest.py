from ..classes import Human, CodeDevelopment, CarMaintenance

import pytest


@pytest.fixture
def human():
    return Human(None)


@pytest.fixture
def mechanic():
    return Human(CarMaintenance())


@pytest.fixture
def developer():
    return Human(CodeDevelopment())
