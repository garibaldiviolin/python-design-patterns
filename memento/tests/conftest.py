from unittest.mock import Mock

from ..classes import (
    Text,
    TextState,
    WordProcessor,
)

import pytest


@pytest.fixture
def text():
    return Text()


@pytest.fixture
def text_mock(text_state_mock):
    text = Mock()
    text.restore_content = Mock()
    text.save_content = Mock(return_value=text_state_mock)
    return text


@pytest.fixture
def text_state():
    return TextState("Look at this!")


@pytest.fixture
def text_state_mock():
    text_state = Mock()
    text_state.get_content = Mock(return_value="Text mocked!")
    return text_state


@pytest.fixture
def word_processor(text_mock):
    return WordProcessor(text_mock)
