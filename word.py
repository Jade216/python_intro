def print_upper_words(words):
    upper_words = []
    for word in words:
        upper_words.append(word.upper())

    return upper_words

def print_upper_words_2(words):
    upper_words = []
    for word in words:
        if word.startswith('e') or word.startswih('E'):
            upper_words.append(word.upper())
    return upper_words

def print_upper_words_3(words, must_start_with):
    upper_word = []
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                upper_word.append(word.upper())

    return upper_word