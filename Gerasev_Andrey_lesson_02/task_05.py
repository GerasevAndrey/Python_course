import copy
import random


def get_price_string(price):
    data = str(price).split('.')
    rub = data[0]
    kop = data[1] if len(data[1]) > 1 else '0' + data[1]

    return f'{rub} руб. {kop} коп.'


random_list_1 = [round(random.uniform(0, 1000), 2) for i in range(20)]

print(', '.join([get_price_string(price) for price in random_list_1]))

random_list_1.sort()
# # Создать новый список, содержащий те же цены, но отсортированные по убыванию.
random_list_2 = random_list_1.copy()
random_list_2.sort(reverse=True)
print(random_list_2)
# Вывести цены пяти самых дорогих товаров.
max_five_in_list = random_list_2[0:5]
print(', '.join([get_price_string(price) for price in max_five_in_list]))
