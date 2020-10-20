from .classes import Text, WordProcessor


text = Text()
word_processor = WordProcessor(text)
word_processor.save()

text.type_word("Look at this lyrics. ")
word_processor.save()

text.type_word("It is a great song.")
word_processor.save()

word_processor.undo()

word_processor.undo()

word_processor.undo()
