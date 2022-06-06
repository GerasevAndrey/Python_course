tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def gen_class():
    for i in range(len(tutors)):
        klass_name = klasses[i] if len(klasses) > i else None
        yield tutors[i], klass_name


for item in gen_class():
    print(item)

# gen = ((tutors[i], klasses[i] if len(klasses) > i else None) for i in range(len(tutors)))

# def gen_class(list_1, list_2):
#     return ((list_1[i], list_2[i] if len(list_2) > i else None) for i in range(len(list_1)))
