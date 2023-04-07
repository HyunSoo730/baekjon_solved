import sys

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
# 0 빈칸 1 집 2 치킨집

#먼저 치킨집 m개 선택
home = []
pizza = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            home.append((i,j))
        if g[i][j] == 2:
            pizza.append((i,j))
k = len(pizza) #피자집 개수
choose = [] #선택한 피자집 인덱스

def min_length(choose):
    length = 0
    for i in range(len(home)): #집을 기준으로
        dis = int(1e9)
        x1,y1 = home[i][0], home[i][1]
        for idx in  choose: #피자집 인덱스 하나씩 꺼내서
            x2,y2 = pizza[idx][0], pizza[idx][1]
            distance = abs(x1-x2) + abs(y1-y2)
            dis = min(dis, distance)
            #i번째 집의 치킨거리 dis로 결정
        length += dis
    return length #선택된 치킨집에 대한 도시의 최소거리 리턴
res = int(1e9)
def DFS(L, start): #
    global res
    if L == m: #피자집 모두 선택했다면 이제 도시의 피자거리 구해야지
        length = min_length(choose)
        res = min(res, length)
    else: #피자집부터 선택
        for i in range(start, k):
            choose.append(i)
            DFS(L+1, i+1) #현재꺼 선택했으면 다음에는 선택 안해야 하므로
            choose.pop()


DFS(0,0)
print(res)