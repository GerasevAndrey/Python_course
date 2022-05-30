def num_translate(eng_word):
    words = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if eng_word in words:  # return words.get(eng_word)
        return words[eng_word]
    return None


# № 1
print(num_translate('one'))


def num_translate_adv(eng_word):
    if eng_word.islower():
        return num_translate(eng_word)

    word = num_translate(eng_word.lower())
    return word.capitalize() if word else None


# № 2
print(num_translate_adv('One'))
