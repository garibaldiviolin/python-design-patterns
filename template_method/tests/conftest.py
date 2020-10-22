from ..classes import Turtle, Bee

import pytest


@pytest.fixture
def turtle():
    return Turtle()


@pytest.fixture
def bee():
    return Bee()
