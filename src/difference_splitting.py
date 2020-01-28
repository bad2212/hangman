from src import UnorderedWords, WordsImporter

word_importer = WordsImporter.WordsImporter()
word_importer.__init__()
words_importer = word_importer.get_words()

words = UnorderedWords.UnorderedWords(words_importer)


def select_top_letter(words):
    hist = words.letter_freq()
    v = list(hist.values())
    k = list(hist.keys())
    l = k[v.index(max(v))]
    return l, hist[l]

def select_middle_letter(words):
    hist = words.letter_freq()
    t = int(words.count()/2)
    best = None
    for k in hist.keys():
        if best is None:
            best = k
        else:
            if abs(hist[k]-t) < abs(hist[best]-t):
                best = k
    return best, hist[best]


guesses = []

while not words.all_letters_equal():
    # print(lst)
    letter, value = select_middle_letter(words)
    guesses.append(letter)
    print(letter, "is in", value, "of", words.count(), "words (" + str(int(100 * value / words.count())) + "%)")
    if value > words.count()/2:
        words.guess_correct(letter)
    else:
        words.guess_wrong(letter)

print("Took", len(guesses), "steps to find these words, guessing:", guesses)
print("\n")

words = UnorderedWords.UnorderedWords(words_importer)
guesses = []

while not words.all_letters_equal():
    # print(lst)
    letter, value = select_top_letter(words)
    guesses.append(letter)
    print(letter, "is in", value, "of", words.count(), "words (" + str(int(100 * value / words.count())) + "%)")
    if value > words.count()/2:
        lst = words.guess_correct(letter)
    else:
        lst = words.guess_wrong(letter)

print("Took", len(guesses), "steps to find these words, guessing:", guesses)
