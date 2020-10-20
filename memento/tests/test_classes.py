from unittest.mock import patch

import pytest

from ..classes import (
    Text,
    TextState,
    WordProcessor,
)


def test_text_initial_content(text):
    assert text._content == ""


def test_text_type_word(text):
    word = "I"
    text.type_word(word)

    assert text._content == word


def test_text_type_two_words(text):
    text.type_word("Word ")
    text.type_word("Processor")

    assert text._content == "Word Processor"


def test_text_save_content(text):
    text._content = "OK!"
    text_state = text.save_content()

    assert isinstance(text_state, TextState) is True
    assert text_state._content == text._content


def test_text_restore_content(text, text_state_mock):
    text.restore_content(text_state_mock)

    assert text._content == "Text mocked!"
    text_state_mock.get_content.assert_called_once_with()


def test_text_state_content(text_state):
    assert text_state._content == "Look at this!"


def test_text_state_get_content(text_state):
    assert text_state.get_content() == "Look at this!"


def test_word_processor_attributes(word_processor, text_mock):
    assert word_processor._text == text_mock
    assert word_processor._text_states == []


@patch("builtins.print")
def test_word_processor_save(print_mock, word_processor, text_mock,
                             text_state_mock):
    word_processor.save()

    assert word_processor._text_states == [text_state_mock]
    text_mock.save_content.assert_called_once_with()
    text_state_mock.get_content.assert_called_once_with()
    print_mock.assert_called_once_with("Saving Text... 'Text mocked!'")


@patch("builtins.print")
def test_word_processor_undo(print_mock, word_processor, text_mock,
                             text_state_mock):
    word_processor._text_states = [text_state_mock]

    word_processor.undo()

    assert word_processor._text_states == []
    text_mock.restore_content.assert_called_once_with(text_state_mock)
    text_state_mock.get_content.assert_called_once_with()
    print_mock.assert_called_once_with("Restoring Text... 'Text mocked!'")


@patch("builtins.print")
def test_word_processor_undo_without_states(print_mock, word_processor,
                                            text_mock, text_state_mock):
    word_processor.undo()

    assert word_processor._text_states == []
    text_mock.restore_content.assert_not_called()
    text_state_mock.get_content.assert_not_called()
    print_mock.assert_not_called()
