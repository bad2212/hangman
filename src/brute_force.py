from src import UnorderedWords, WordsImporter

word_importer = WordsImporter.WordsImporter()
word_importer.__init__()
words_importer = word_importer.get_words()

words = UnorderedWords.UnorderedWords(words_importer)

while not words.all_letters_equal():
    print(words.words)
    letter = words.get_most_common_letter()
    print(letter)
    words.guess_correct(letter)