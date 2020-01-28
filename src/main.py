#words source: https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt
from src import UnorderedWords, WordsImporter

word_importer = WordsImporter.WordsImporter()
word_importer.__init__()
word_importer.get_words_of_length(5)
words = UnorderedWords.UnorderedWords(word_importer.get_words_of_length(5))

words.print_words()
