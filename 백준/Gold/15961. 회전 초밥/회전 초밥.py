from collections import defaultdict
n,d,k,c = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))

dic = defaultdict(int)
start = 0
end = k-1

for i in range(k-1):
    dic[data[i]] += 1
# 첫번째 윈도우 세팅하고 시작

res = 0
# 원형이므로 %n 처리 해줘야함 !!! -> 아니면 기존 배열 data 에 이어 붙여서 처리해야함
while end < n + k -1:
    dic[data[end%n]] += 1  # 끝점 추가 후 계산 진행
    if c in dic.keys():
        res = max(res, len(dic))
    else:
        res = max(res, len(dic) + 1)
    # 체크했으니
    dic[data[start%n]] -= 1
    if dic[data[start%n]] == 0:
        dic.pop(data[start%n])
    start += 1
    end += 1  # 끝점 역시 while 문이기에 증가시켜줌

print(res)