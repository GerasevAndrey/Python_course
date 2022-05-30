def thesaurus(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(thesaurus('Андрей', 'Анна', 'Максим', 'Мария', 'Олег'))


def thesaurus_adv(*names):
    res = {}

    for name in names:
        first_name, last_name = name.split()

        if last_name[0] in res:
            res[last_name[0]].append(name)
        else:
            res[last_name[0]] = [name]

    for key, value in res.items():
        res[key] = thesaurus(*value)

    return res


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
