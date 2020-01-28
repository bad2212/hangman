import string


class UnorderedWords:
    words = []

    def __init__(self, words):
        self.words = words

    def print_words(self):
        for (a, _) in self.words:
            print(a)

    def count(self):
        return len(self.words)

    def letter_freq(self):
        hist = {}
        for letter in string.ascii_lowercase:
            hist[letter] = 0
        for (word, letters) in self.words:
            for letter in string.ascii_lowercase:
                if letter in letters:
                    hist[letter] += 1
        return hist

    def all_letters_equal(self):
        if not self.words:
            return True
        lst = self.words[0][1]
        for i in self.words:
            if not i[1] == lst:
                return False
        return True

    def get_most_common_letter(self):
        hist = self.letter_freq()
        v = list(hist.values())
        k = list(hist.keys())
        return k[v.index(max(v))]

    def guess_correct(self, letter):
        subwords = []
        for (word, letters) in self.words:
            if letter in word:
                letters.remove(letter)
                if len(letters) > 0:
                    subwords.append((word, letters))
        self.words = subwords

    def guess_wrong(self, letter):
        subwords = []
        for (word, letters) in self.words:
            if letter not in word:
                subwords.append((word, letters))
        self.words = subwords

    def guess_by_instruction(self, letters_to_guess):
        for (l, b) in letters_to_guess:
            if b:
                self.guess_correct(l)
            else:
                self.guess_wrong(l)
            print(self.words)

    def get_words(self):
        return self.words