import sys

# sys.stdin = open("input.text", "rt")

N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

temp = data[0]
count = 0
while True:
    if len(data) == 1:  #본인만
        break
    max_data = max(data[1:])
    if max_data >= temp:  
        for i in range(1, len(data)):
            if data[i] == max_data:
                data[i] -=1 
                temp += 1
                count += 1
                break
    if temp > max(data[1:]):
        break

print(count)

