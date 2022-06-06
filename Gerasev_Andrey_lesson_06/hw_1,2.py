import os


def get_log(txt_file="./nginx_logs.txt"):
    if os.path.isfile(txt_file):
        with open(txt_file, "r", encoding="utf-8") as file:
            for line in file:
                data = line.split()
                yield data[0], data[5][1:], data[6]


# 2

def find_spam(logs):
    tp = {}
    result = {'ip': None, 'count': 0}
    for log in logs:
        tp[log[0]] = tp.get(log[0], 0) + 1
        if tp[log[0]] > result.get('count'):
            result = {'ip': log[0], 'count': tp[log[0]]}
    return result


if __name__ == "__main__":
    parsed = get_log()
    for i in range(5):
        print(next(parsed))

    spam = find_spam(parsed)
    if spam:
        print(f"ip spam: {spam.get('ip')}, count: {spam.get('count')}")
