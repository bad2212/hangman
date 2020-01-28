import string


def counts_as_word(w):
    if len(w) < 2:
        return False
    for l in w:
        if l not in string.ascii_lowercase:
            return False
    return True


class WordsImporter:
    words = {}

    def __init__(self):
        for word in open("words", "r").readlines():
            word = word[:-1]
            if counts_as_word(word):
                if len(word) not in self.words:
                    self.words[len(word)] = []
                if set(list(word)) not in self.words[len(word)]:
                    self.words[len(word)].append((word, set(list(word))))

    def get_words_of_length(self, length):
        return self.words[length]

    def get_words(self):
        return self.words[6]
