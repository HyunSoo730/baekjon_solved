import sys


data = input()
data = data.upper()

res = dict()
for x in data:
    if x in res.keys():
        res[x] += 1
    else:
        res[x] = 1

temp = res.values()
max_data = max(temp)
cnt = 0
for x in temp:
    if x == max_data:
        cnt += 1

result = ""
for key, value in res.items():
    if value == max_data:
        result = key

if cnt >= 2:
    print("?")
else:
    print(result)











