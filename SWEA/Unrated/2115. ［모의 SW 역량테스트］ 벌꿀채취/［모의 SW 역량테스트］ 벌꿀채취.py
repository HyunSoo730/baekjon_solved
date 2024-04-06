
### nxn 벌통
# 각 칸은 꿀의 양
# 두명의 일꾼. 가로로 M개의 칸 선택 겹치면 안된다.
# 완탐. 전부 확인 -> 백트랙킹으로 구현 가능 일꾼1 선택 후 일꾼 2
# 각 꿀통 최대 C

def DFS(L, sum_value, sum_pow, x,y):
    global max_data
    if sum_value > c: # 합친 꿀의 양이 c보다 큰 경우 가지치기
        return
    if L == m:
         max_data = max(max_data, sum_pow)
    else:
        DFS(L+1, sum_value + g[x][y+L], sum_pow + g[x][y+L] ** 2 , x, y)
        DFS(L+1, sum_value, sum_pow, x,y)




T = int(input())
for t in range(1,T+1):
    n,m,c = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    sumA = sumB = 0
    res = 0
    max_data = 0
    for x1 in range(n): # 일꾼1의 행
        for y1 in range(n-m+1): # 일꾼1의 시작 열
            max_data = 0
            DFS(0,0,0,x1,y1)
            sumA = max_data # 현재 좌표에서 m개의 칸 확인할 때의 일꾼A의 최대값
            for x2 in range(x1, n): # 일꾼1의 행부터 시작 가능 !
                start = 0
                if x1 == x2: start = y1 + m
                else: start = 0 # 다른 행이면 0번쨰 열부터 시작 가능
                for y2 in range(start, n-m+1):     ### 여기까지가 가능한 두 일꾼의 위치!!!!
                    # 시작좌표 기준 m개 가능한 모든 선택 !!
                    max_data = 0
                    DFS(0,0,0,x2,y2)
                    res = max(res, sumA + max_data) # 현재 좌표에서 일꾼 2의 최댓값이 max_data에 기록. 
    print(f"#{t} {res}")


