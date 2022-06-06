import os
from sys import argv

LOG_PATH = './sales.log'
if __name__ == '__main__':
    params = argv[1:]
    if len(params) != 1:
        exit('invalid params')

    if not os.path.isfile(LOG_PATH):
        with open(LOG_PATH, 'w', encoding='utf-8') as f:
            f.write(f'{params[0]}\n')
    else:
        with open(LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(f'{params[0]}\n')
