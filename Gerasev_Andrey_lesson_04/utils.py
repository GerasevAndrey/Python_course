from xml.etree import ElementTree

import datetime
import requests
from decimal import Decimal


def currency_rates(char_code):
    if len(char_code) != 3:
        return None

    char_code = char_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    tree = ElementTree.XML(response.text)
    for item in tree:
        if char_code == item[1].text:
            price = item[4].text.replace(',', '.')
            value = Decimal(price).quantize(Decimal('1.00'))
            date = tree.get("Date").split('.')
            return value, datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2]))
