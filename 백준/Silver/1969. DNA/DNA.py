import sys



#DNA 리스트를 열 단위로 봤을 때 가장 많은 것을 하나씩 고르는 문제였음. 문제이해를 제대로 못했음
#해밍 distance가 가장 작아야 하므로 같은게 가장 많아야함.

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(input())

res = []
cnt = 0
for i in range(M):   #열을 기준으로 확인해야 하므로 
    count = [0,0,0,0]   #A C G T    같다면 사전순 반환해야해서.   
    for j in range(N):
        if data[j][i] == "A":
            count[0] += 1
        elif data[j][i] == "C":
            count[1] += 1
        elif data[j][i] == "G":
            count[2] += 1
        elif data[j][i] == "T":
            count[3] += 1   
    idx = count.index(max(count))   #가장 큰 값의 인덱스를 반환. 
  #  index메서드는 지정 값이 처음으로 나오는 값을 반환 그렇기에 사전순 가능! 없는 경우 에러. fnid는 똑같지만 없는경우 -1반환
    if idx == 0:
        res.append("A")
    elif idx == 1:
        res.append("C")
    elif idx == 2:
        res.append("G")
    elif idx == 3:
        res.append("T")
    cnt += N - max(count)

for x in res:
    print(x, end = "")
print()
print(cnt)