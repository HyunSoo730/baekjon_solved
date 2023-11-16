from collections import deque

T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split())
    data = list(map(int, input().split())) # n명의 사람들이 도착하는 시간
    data.sort() # 오름차순 정렬
    cnt = 0
    e = data[-1] # 가장 마지막에 도착하는 사람의 시간
    dq = deque(data)
    for i in range(e+1):
        if i != 0 and i % m == 0:
            cnt += k
        if dq[0] == i: # 현재 초에 방문
            if cnt > 0:
                cnt -= 1
                dq.popleft() # 해당 사람 통과
            else:
                print(f"#{t} Impossible")
                break
    else:
        print(f"#{t} Possible")

