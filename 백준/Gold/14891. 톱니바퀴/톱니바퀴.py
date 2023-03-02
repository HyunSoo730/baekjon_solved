import sys
from collections import deque

data = []
for _ in range(4):
    temp = list(map(int, input()))
    data.append(temp)
data.insert(0,-1)
#4개의 톱니바퀴 저장
#12시방향부터 시계방향순으로 순서대로 주어진다. (8개)
k = int(input()) #회전횟수
rot = []
for _ in range(k):
    a,b = map(int, input().split())
    rot.append((a,b)) #회전시킬 톱니 번호, 방향

# print([data[1][0]])
# a = [data[1][0]]
# b = data[1][1:8]
# print(a,b)
# print(data[1])
# print(b+a)

#k번 회전 후 점수 합
def BFS(v, r): #톱니 번호, 방향
    dq = deque()
    dq.append((v,r))
    ch = [0] * 5
    ch[v] = 1
    while dq:
        now,rot = dq.popleft() #현재 톱니 번호, 회전 방향
        left = data[now][6]  #현재 톱니의 왼쪽
        right = data[now][2] #오른쪽
        if rot == 1: #시계
            data[now] = [data[now][7]] + data[now][:7] #시계 방향 회전
        elif rot == -1: #반시계
            data[now] = data[now][1:8] + [data[now][0]]
        #현재 톱니 회전 끝났다면 인접 톱니들 확인
        if now-1>=1 and ch[now-1] == 0: #왼쪽 탐색 가능, 방문 가능
            if data[now-1][2] != left: #같지 않은 경우만 회전
                ch[now-1] = 1
                dq.append((now-1, rot*-1)) #반대방향으로 회전해야 하므로
        if now+1<=4 and ch[now+1] ==0:
            if data[now+1][6] != right:
                ch[now+1] = 1
                dq.append((now+1, rot*-1))
    


for i in range(k):
    a,b = rot[i][0], rot[i][1] #번호, 방향
    #톱니바퀴의 0번 인덱스는 12시 방향.
    #왼쪽은 6번 인덱스, 오른쪽은 2번 인덱스
    BFS(a,b)

# for i in range(1,5):
#     print(data[i][0])

t = [1,2,4,8]
cnt = 0
for i in range(1,5):
    if data[i][0] == 1:
        cnt += t[i-1]
print(cnt)

    