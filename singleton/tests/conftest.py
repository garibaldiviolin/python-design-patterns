import pytest

from ..classes import Configuration


@pytest.fixture
def configuration():
    return Configuration.get_instance()


@pytest.fixture
def configuration2():
    return Configuration.get_instance()
