from unittest.mock import Mock

from builder.classes import ConcreteHouseBuilder, Foreman, House

import pytest


@pytest.fixture
def new_house():
    return House()


@pytest.fixture
def builder():
    return ConcreteHouseBuilder()


@pytest.fixture
def builder_mock(new_house):
    builder = Mock()
    builder.start_house = Mock()
    builder.add_bedrooms = Mock()
    builder.add_living_rooms = Mock()
    builder.house = new_house
    return builder


@pytest.fixture
def foreman(builder):
    return Foreman(builder)
