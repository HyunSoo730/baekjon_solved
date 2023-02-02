import sys



N = int(input())
res = 0
money = []
for i in range(N):
    money.append(int(input()))
    
money.sort(reverse=True)

for i in range(N):
    if money[i] - (i+1 - 1) < 0:
        continue
    res += money[i] - (i)

print(res)
