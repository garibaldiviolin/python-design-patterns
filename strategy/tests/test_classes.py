from unittest.mock import Mock, patch

import pytest

from strategy.classes import Human


def test_work():
    activity_mock = Mock()
    activity_mock.do = Mock()

    human = Human(activity_mock)
    human.work()

    activity_mock.do.assert_called_once_with()


def test_work_without_activity(human):
    """Tests a Human object with activity=None."""
    with pytest.raises(AttributeError):
        human.work()


@patch('builtins.print')
def test_talk(print_mock, human):
    human.talk()

    print_mock.assert_called_once_with("Talking...")


@patch('builtins.print')
def test_developer_work(print_mock, developer):
    """Tests the CodeDevelopment class."""
    developer.work()

    print_mock.assert_called_once_with("Developing some code...")


@patch('builtins.print')
def test_mechanic_work(print_mock, mechanic):
    """Tests the CarMaintenance class."""
    mechanic.work()

    print_mock.assert_called_once_with("Repairing the car...")
