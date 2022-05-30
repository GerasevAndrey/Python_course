from utils import currency_rates
from sys import argv

val = argv[1] if len(argv) > 1 else input("Введите код валюты ")
print(*currency_rates(val), sep=', ')
