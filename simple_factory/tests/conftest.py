from simple_factory.classes import AnimalFactory

import pytest


@pytest.fixture
def duck():
    return AnimalFactory.create_animal("duck")


@pytest.fixture
def lion():
    return AnimalFactory.create_animal("lion")
