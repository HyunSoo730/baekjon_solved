import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
avg = round(sum(data) / n)
mid = data[n//2]

#최빈값 딕셔너리로
res = dict()
for i in range(len(data)):
    if data[i] in res.keys():
        res[data[i]] += 1
    else:
        res[data[i]] = 1
max_data = max(res.values())
cnt = 0
tt = []
for key, val in res.items():
    if val == max_data:
        cnt += 1
        tt.append(key)

if cnt >= 2:
    most = tt[1]
else:
    most = tt[0] #어차피 tt에 최빈값 저장되니깐. 0번에 딱 하나 저장되어 있을 것.


# data_set = list(set(data))
# data_set.sort()
# cnt = []
# for x in data_set:
#     count = data.count(x)
#     cnt.append(count)
# #cnt에 개수 같은게 여러개라면 두번째로 작은거.
# temp = max(cnt)
# c = cnt.count(temp)
# if c >= 2: #같은거 2개이상인 경우 두번째로 작은거 찾아야함
#     ss = []
#     for i in range(len(data_set)):
#         if cnt[i] == temp:
#             ss.append(data_set[i])
#     most = ss[1]
# else: #가장큰거 한개인 경우.
#     most = data_set[cnt.index(temp)]

    
ran = data[-1] - data[0]
print(avg)
print(mid)
print(most)
print(ran)
    





