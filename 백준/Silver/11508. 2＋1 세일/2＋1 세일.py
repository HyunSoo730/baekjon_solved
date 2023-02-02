import sys



N = int(input())
data = []
for i in range(N):
    data.append(int(input()))


data.sort(reverse = True)
sum = 0
for i in range(N):
    if (i+1) % 3 == 0:
        continue
    sum += data[i]

print(sum)