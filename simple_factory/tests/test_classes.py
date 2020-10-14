from unittest.mock import patch

import pytest

from simple_factory.classes import AnimalFactory, Lion, Duck


@pytest.mark.parametrize("species,animal_class", [
    ("duck", Duck),
    ("lion", Lion),
])
def test_create_animal(species, animal_class):
    animal = AnimalFactory.create_animal(species)
    assert isinstance(animal, animal_class)


def test_create_invalid_animal():
    with pytest.raises(KeyError):
        AnimalFactory.create_animal("virus")


def test_duck_class(duck):
    assert isinstance(duck, Duck) is True


@patch("builtins.print")
def test_duck_quack(print_mock, duck):
    duck.quack()
    print_mock.assert_called_once_with("Quack quack...")


def test_lion_class(lion):
    assert isinstance(lion, Lion) is True


@patch("builtins.print")
def test_lion_roar(print_mock, lion):
    lion.roar()
    print_mock.assert_called_once_with("Roaring...")
