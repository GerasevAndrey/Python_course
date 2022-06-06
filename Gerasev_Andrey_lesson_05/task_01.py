def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


def odd_nums_2(max_num):
    return (num for num in range(1, max_num + 1, 2))


odd_to_15 = odd_nums(15)
odd_to_15_2 = odd_nums_2(15)
try:
    print(next(odd_to_15))
    next(odd_to_15)
    print(next(odd_to_15))
    next(odd_to_15)
    print(next(odd_to_15))
    next(odd_to_15)
    print(next(odd_to_15))
    next(odd_to_15)
    print(next(odd_to_15))
except StopIteration:
    print('StopIteration')
