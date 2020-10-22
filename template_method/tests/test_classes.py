from unittest.mock import patch, call

import pytest

from ..classes import LivingBeing


def test_create_living_being_instance():
    with pytest.raises(TypeError) as exc:
        LivingBeing()

    assert str(exc.value) == (
        "Can't instantiate abstract class LivingBeing with abstract methods "
        "be_born, die, live"
    )


@patch("builtins.print")
def test_turtle_do_life_cycle(print_mock, turtle):
    turtle.do_life_cycle()

    assert print_mock.mock_calls == [
        call("A turtle was born."),
        call("This turtle lives and is 150 years old."),
        call("The turtle has died."),
    ]


@patch("builtins.print")
def test_bee_do_life_cycle(print_mock, bee):
    bee.do_life_cycle()

    assert print_mock.mock_calls == [
        call("A bee was just born."),
        call("The bee has been alive for 5 days."),
        call("Unfortunately, this bee has just died."),
    ]
