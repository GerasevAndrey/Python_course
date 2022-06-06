import json
import os
from sys import argv


def get_parse(
        user_pth="./users.csv",
        hobby_pth="./hobbies.csv"):
    user_lines = []
    hobby_lines = []

    if not os.path.isfile(user_pth) or not os.path.isfile(hobby_pth):
        exit('file not found')

    with open(user_pth, "r", encoding="utf-8") as user_file:
        for user in user_file:
            l_name, f_name, m_name = user.strip().split(',')

            user_lines.append({'l_name': l_name, 'f_name': f_name, 'm_name': m_name})

    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        for hobby in hobby_file:
            hobby_lines.append(hobby.strip().split(','))

    if len(user_lines) < len(hobby_lines):
        exit(1)

    for i in range(len(user_lines)):
        hobby = hobby_lines[i] if len(hobby_lines) > i else None
        user_lines[i]['hobbies'] = hobby
    return user_lines


if __name__ == '__main__':
    params = argv[1:]
    if len(params) < 3:
        exit('params not valid')

    data = get_parse(params[0], params[1])
    print(__file__)
    with open(params[2], 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
