from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def get_num(*argv):
    num_list = set()

    for elem in argv:
        if elem not in num_list:
            num_list.add(elem)
        else:
            num_list.remove(elem)

    return [x for x in argv if x in num_list]


start = perf_counter()
result = get_num(*src)
finish = perf_counter()
print(result, finish - start)

start = perf_counter()
result = [item for item in src if src.count(item) == 1]
finish = perf_counter()
print(result, finish - start)
