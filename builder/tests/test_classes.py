from builder.classes import HouseBuilder

import pytest


def test_create_abstract_house_builder():
    with pytest.raises(TypeError) as exc:
        HouseBuilder()

    assert str(exc.value) == (
        "Can't instantiate abstract class HouseBuilder with abstract "
        "methods add_bathroom, add_bedroom, built_house, start_house"
    )


def validate_new_house(house):
    assert hasattr(house, "bedrooms") is False
    assert hasattr(house, "bathrooms") is False
    assert hasattr(house, "living_rooms") is False


def test_new_house(new_house):
    validate_new_house(new_house)


def test_builder_start_house(builder):
    builder.start_house()
    validate_new_house(builder.house)


def test_add_first_bathrooms(new_house, builder):
    builder._house = new_house
    builder.add_bathrooms(2)
    assert new_house.bathrooms == 2


def test_add_more_bathrooms(new_house, builder):
    builder._house = new_house
    builder.add_bathrooms(2)
    builder.add_bathrooms(1)  # add one more bathroom
    assert new_house.bathrooms == 3


def test_add_first_bedrooms(new_house, builder):
    builder._house = new_house
    builder.add_bedrooms(5)
    assert new_house.bedrooms == 5


def test_add_more_bedrooms(new_house, builder):
    builder._house = new_house
    builder.add_bedrooms(5)
    builder.add_bedrooms(2)  # add two more bedrooms
    assert new_house.bedrooms == 7


def test_add_first_living_rooms(new_house, builder):
    builder._house = new_house
    builder.add_living_rooms(3)
    assert new_house.living_rooms == 3


def test_add_more_living_rooms(new_house, builder):
    builder._house = new_house
    builder.add_living_rooms(1)
    builder.add_living_rooms(1)  # add one more living room
    assert new_house.living_rooms == 2


def test_builder_house_property(new_house, builder):
    builder._house = new_house
    assert builder.house == new_house


def test_foreman_house_builder(foreman, builder):
    assert foreman._house_builder == builder


def test_build_mansion(foreman, builder_mock, new_house):
    foreman._house_builder = builder_mock

    mansion = foreman.build_mansion()
    builder_mock.start_house.assert_called_once_with()
    builder_mock.add_bedrooms.assert_called_once_with(10)
    builder_mock.add_bathrooms.assert_called_once_with(10)
    builder_mock.add_living_rooms.assert_called_once_with(1)

    assert mansion == new_house


def test_build_small_house(foreman, builder_mock, new_house):
    foreman._house_builder = builder_mock

    small_house = foreman.build_small_house()
    builder_mock.start_house.assert_called_once_with()
    builder_mock.add_bedrooms.assert_called_once_with(1)
    builder_mock.add_bathrooms.assert_called_once_with(1)
    builder_mock.add_living_rooms.assert_not_called()

    assert small_house == new_house
