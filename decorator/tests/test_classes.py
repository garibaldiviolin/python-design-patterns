from unittest.mock import patch, call


def test_algorithm_numbers(algorithm, numbers):
    assert algorithm.numbers == numbers


def test_algorithm_calculate(algorithm, calculate):
    assert algorithm.calculate() == calculate


def test_logged_algorithm(logged_algorithm, algorithm_mock):
    assert logged_algorithm.algorithm == algorithm_mock


@patch("builtins.print")
def test_logged_algorithm_calculate(print_mock, logged_algorithm,
                                    algorithm_mock, calculate_mock):
    result = logged_algorithm.calculate()

    assert result == calculate_mock
    algorithm_mock.calculate.assert_called_with()
    assert print_mock.mock_calls == [
        call("Calling calculate operation..."),
        call("The result is 9153834."),
    ]
