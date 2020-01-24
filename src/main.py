#words source: https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt
import string


def counts_as_word(w):
    if len(w) < 2:
        return False
    for l in w:
        if l not in string.ascii_lowercase:
            return False
    return True


def letter_freq(words):
    hist = {}
    for letter in string.ascii_lowercase:
        hist[letter] = 0
    for (word, letters) in words:
        for letter in string.ascii_lowercase:
            if letter in letters:
                hist[letter] += 1
    return hist


def all_letters_equal(words):
    return words == []
    # hist = letter_freq(words)
    # v = list(hist.values())
    # if max(v) == min(v):
    #     print(words)
    #     print(hist)
    # return max(v) == min(v)


def is_done(words):
    return False


def most_common_letter(words):
    hist = letter_freq(words)
    v = list(hist.values())
    k = list(hist.keys())
    return k[v.index(max(v))]


def remove_letter(words, letter):
    subwords = []
    for (word, letters) in words:
        if letter in word:
            letters.remove(letter)
            subwords.append((word, letters))
    return subwords


def all_without_letter(words, letter):
    subwords = []
    for (word, letters) in words:
        if letter not in word:
            subwords.append((word, letters))
    return subwords


def remove_most_common_letter(words):
    letter = most_common_letter(words)
    return remove_letter(words, letter)


def all_without_most_common_letter(words):
    letter = most_common_letter(words)
    return all_without_letter(words, letter)


def handle_letter(words, remove):
    if remove:
        return remove_most_common_letter(words)
    else:
        return all_without_most_common_letter(words)


def guess_by_instruction(words, letters_to_guess):
    for (l, b) in letters_to_guess:
        if b:
            words = remove_letter(words, l)
        else:
            words = all_without_letter(words, l)
        print(words)
    return words

# Store words in a dictionary, into lists based on word length
words = {}
for word in open("words", "r").readlines():
    word = word[:-1]
    if counts_as_word(word):
        if len(word) not in words:
            words[len(word)] = []
        if set(list(word)) not in words[len(word)]:
            words[len(word)].append((word, set(list(word))))

# Prints how many words exist of each length
# for i in words.keys():
#    print(str(i) + ": " + str(len(words[i])))

to_remove = False
word_length = 7

lst = words[word_length]

# One approach to the problem, guessing until there are no words for which a letter hasn't been guessed
while not all_letters_equal(handle_letter(lst, to_remove)):
    print(lst)
    print(most_common_letter(lst))
    lst = handle_letter(lst, to_remove)

# Print the words remaining before the last guess
for (a, _) in lst:
    print(a)

# Each tuple represents a guessed letter and whether or not to treat it as correct
guesses = [('e', False), ('a', False), ('o', True), ('i', False), ('u', True)]

# The list of six letter words
lst = words[6]

# Update the list of words by making guesses
lst = guess_by_instruction(lst, guesses)

# Prints the words remaining
for (a, _) in lst:
    print(a)

# Todo: Think about letter ordering. Would require moving away from sets and allowing wildcards
