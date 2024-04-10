
# nxn 벌통, 각각의 칸은 벌통의 꿀의 양.
# 최대한 많은 수익 얻기.
# 두 명의 일꿀. 각각 가로로 연속되도록 M개의 벌통 선택. 선택한 벌통에서 꿀 채취
# 두 명은 서로 겹치면 안됨.
# 각 일꾼들은 선택한 벌통서 꿀 채취 -> 최대 C까지 채취 # 넘어가면 그 중 일부만.
# 구하고자 : 두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대가 되는 경우. 그때의 수익

# 일단. 두 일꾼이 시작 좌표부터 픽스.
# 선택한 M개 벌통 중 모든 경우의 수 확인해서 C를 넘지 않는 최대 값 찾기 -> 부분집합

def DFS(L, sum_data, value,x,y):
    global res
    if sum_data > c:
        return
    if L == m: # m개 모두 확인
        res = max(res, value)
    else:
        DFS(L+1, sum_data + g[x][y+L], value + g[x][y+L] ** 2, x, y)
        DFS(L+1, sum_data, value, x,y)

T = int(input())
for t in range(1,T+1):
    n,m,c = map(int, input().split()) # 별통 크기 n, 채취하는 가로 길이 m, 최대 양 C
    g = [list(map(int, input().split())) for _ in range(n)]
    # 일꾼 1부터 시작 위치 픽스
    sumA = sumB = 0
    result = 0
    for x in range(n):
        for y in range(n-m+1): # 즉 가장 마지막 좌표부터 m개 채취해야 하므로
            # (x,y)가 일꾼 1의 시작 위치
            res = 0
            DFS(0, 0, 0,x,y) # 현재 위치도 함께
            sumA = res # 기억
            # 일꾼1에 대한 최대값 구했으니 일꾼2의 값 구하기
            for x2 in range(x, n): # 일꾼 2는 일꾼1과 같은 행부터 가능
                start = 0
                if x == x2:
                    start = y+m
                else:
                    start = 0
                for y2 in range(start,n-m+1):
                    res = 0
                    DFS(0,0,0,x2,y2)
                    sumB = res
                    result = max(result, sumA + sumB)
    print(f"#{t} {result}")
