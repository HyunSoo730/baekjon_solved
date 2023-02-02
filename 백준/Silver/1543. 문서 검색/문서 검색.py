import sys



data = input()
want = input()

cnt = 0
while True:
    index = data.find(want)
    if index == -1:
        break
    cnt += 1

    data = data[index + len(want):]

print(cnt)

