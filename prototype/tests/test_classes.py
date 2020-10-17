from unittest.mock import patch

from ..classes import Sheep


def test_sheep_clone(sheep2):
    assert isinstance(sheep2, Sheep) is True
    assert sheep2.name == "Lucky"


@patch("builtins.print")
def test_sheep_sound(print_mock, sheep2):
    sheep2.sound()
    print_mock.assert_called_once_with('Lucky: "Baa..."')
