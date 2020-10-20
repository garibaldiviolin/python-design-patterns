from queue import Queue, Empty


class Text:
    """This class (Originator) is the current text of the word
    processor.
    """
    def __init__(self):
        self._content = ""

    def type_word(self, word):
        self._content += word

    def save_content(self):
        return TextState(self._content)

    def restore_content(self, text_state):
        self._content = text_state.get_content()


class TextState:
    """This class (Memento) is responsible for storing the Text class
    state.
    """
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


class WordProcessor:
    """This class (Caretaker) is responsible for saving and restoring
    all of the TextStates.
    """
    def __init__(self, text):
        self._text = text
        self._text_states = list()

    def save(self):
        text_state = self._text.save_content()
        print(f"Saving Text... '{text_state.get_content()}'")
        self._text_states.append(text_state)

    def undo(self):
        try:
            text_state = self._text_states.pop()
        except IndexError:
            return

        print(f"Restoring Text... '{text_state.get_content()}'")
        self._text.restore_content(text_state)
