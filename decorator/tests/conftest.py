from unittest.mock import MagicMock, Mock

import pytest

from ..classes import Algorithm, LoggedAlgorithm


@pytest.fixture
def numbers():
    return (5, 4, 3)


@pytest.fixture
def calculate():
    return 12


@pytest.fixture
def algorithm(numbers):
    return Algorithm(*numbers)


@pytest.fixture
def calculate_mock():
    return 9_153_834


@pytest.fixture
def algorithm_mock(calculate_mock):
    algorithm = MagicMock()
    algorithm.calculate = Mock(return_value=calculate_mock)
    return algorithm


@pytest.fixture
def logged_algorithm(algorithm_mock):
    logged_algorithm = LoggedAlgorithm(algorithm_mock)
    return logged_algorithm
