def get_percent_text(number):
    num = number % 100

    if 10 <= num <= 19:
        return f'{number} процентов'

    num = number % 10

    if num == 1:
        return f'{number} процент'

    if 1 < num < 5:
        return f'{number} процента'

    return f'{number} процентов'


for i in range(100):
    print(get_percent_text(i + 1))
