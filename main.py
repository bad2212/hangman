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


words = {}
for word in open("words", "r").readlines():
    word = word[:-1]
    if counts_as_word(word):
        if len(word) not in words:
            words[len(word)] = []
        if set(list(word)) not in words[len(word)]:
            words[len(word)].append((word, set(list(word))))

for i in words.keys():
    print(str(i) + ": " + str(len(words[i])))

to_remove = False
word_length = 6

lst = words[word_length]

# t_list = words[word_length]
# print(t_list)
#
# print(most_common_letter(t_list))
#
# one_pass = handle_letter(t_list, to_remove)
#
# print(one_pass)
#
# print(most_common_letter(one_pass))
#
# two_pass = handle_letter(one_pass, to_remove)
#
# print(two_pass)
#
# print(most_common_letter(two_pass))
#
# three_pass = handle_letter(two_pass, to_remove)
#
# print(three_pass)
#
# print(most_common_letter(three_pass))
#
# four_pass = handle_letter(three_pass, to_remove)
#
# print(four_pass)
#
# print(most_common_letter(four_pass))
#
# five_pass = handle_letter(four_pass, to_remove)
#
# print(five_pass)
#
# print(most_common_letter(five_pass))
#
# six_pass = handle_letter(five_pass, to_remove)
#
# print(six_pass)


while not all_letters_equal(handle_letter(lst, to_remove)):
    print(lst)
    print(most_common_letter(lst))
    lst = handle_letter(lst, to_remove)

for (a, b) in lst:
    print(a)


# Todo: Think about letter ordering. Would require moving away from sets and allowing wildcards
# Todo: Allow for user to input letter guesses and see remaining words
