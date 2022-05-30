def get_divide(numbers):
    result = 0
    for number in numbers:
        total = 0

        for i in range(len(str(number))):
            total += int(str(number)[i])

        if total % 7 == 0:
            result += number

    return result


if __name__ == "__main__":
    cubes = [x ** 3 for x in range(1000) if not x % 2 == 0]
    print(get_divide(cubes))

    cubes_2 = [x + 17 for x in cubes]
    print(get_divide(cubes_2))

