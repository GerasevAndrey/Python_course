from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
s = perf_counter()
result = []
for i in range(len(src) - 1):
    prev = src[i]
    curr = src[i + 1]
    if curr > prev:
        result.append(curr)
f = perf_counter()
print(result, f - s)
s = perf_counter()
res_list = [num1 for num1, num2 in zip(src[1:], src[:-1]) if num1 > num2]
f = perf_counter()
print(res_list, f - s)
