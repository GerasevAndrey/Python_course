from random import choice, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeats=True):
    if not repeats and n > min(len(adverbs), len(nouns), len(adjectives)):
        return None

    if repeats:
        return [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for i in range(n)]

    nouns_list = sample(range(len(nouns)), n)
    adverbs_list = sample(range(len(adverbs)), n)
    adjectives_list = sample(range(len(adjectives)), n)

    return [f'{nouns[nouns_list[i]]} {adverbs[adverbs_list[i]]} {adjectives[adjectives_list[i]]}' for i in range(n)]


print(get_jokes(5, repeats=False))
