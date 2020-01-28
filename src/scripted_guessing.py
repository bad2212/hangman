from src import UnorderedWords, WordsImporter

word_importer = WordsImporter.WordsImporter()
word_importer.__init__()
words_importer = word_importer.get_words()

words = UnorderedWords.UnorderedWords(words_importer)


# What happens when you try to guess a six letter word where the only vowel is u?
guesses = [('e', False), ('a', False), ('o', False), ('i', False), ('u', True)]

words.guess_by_instruction(guesses)
words.print_words()