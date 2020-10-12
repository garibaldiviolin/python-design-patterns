import pytest

from singleton.classes import Configuration


def test_configuration_constructor():
    with pytest.raises(AttributeError) as exc:
        Configuration()

    assert str(exc.value) == (
        "You cannot instantiate Configuration class. "
        "Please use get_instance method."
    )


def test_instances_ids(configuration, configuration2):
    assert id(configuration) == id(configuration2)


def test_configuration_attribute(configuration, configuration2):
    configuration.api_timeout = 2

    assert configuration2.api_timeout == 2
