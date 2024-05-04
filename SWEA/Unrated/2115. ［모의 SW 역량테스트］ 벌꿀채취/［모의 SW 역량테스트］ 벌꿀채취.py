

# nxn 맵, 각 칸은 각각의 벌통에 있는 꿀의 양 나타냄. 꿀의 양 다를 수 있음
# 최대한 많은 꿀의 양 채취하기
# 2명의 일꾼들이 각각 채취할 수 있는 벌통의 수 m 존재
# 가로로 연속되도록 m개의 벌통 선택. 선택한 벌통에서 꿀 채취 가능, 2명의 일꾼이 선택한 벌통 겹치면 안됨
# 두 일꾼이 채취할 수 있는 꿀의 최대 양 C

# 벌통들의 크기 n, 벌통들 정보 g, 선택할 수 있는 개수 m, 꿀을 채취할 수 있는 최대 양 C
# 최대로 얻을 수 있는 수익의 합 찾기 : 수익 : 꿀을 채취할 수 있는 경우 제곱의 합으로 구하기

# 1. 첫번쨰 사람 먼저 벌통 선택.
# 첫번째 사람의 채취 시작 위치를 먼저 정하기 (무조건 가로로 m개 선택)
# 행은 처음부터 끝까지, 열은 n-m까지 가능. (n-m부터 m개 선택 시 n-1이니까)
# 2. 두번째 사람 선택.
# 두번째 사람은 첫번째 사람이 선택한 이후부터 선택을 진행

def DFS(L, x, y, sum_data, 수익):  # 벌꿀 채취 위지, 현재까지의 벌꿀 합 (c보다 작아야), 수익
    global res
    if sum_data > c:  # 최대치 초과 시 안됨
        return
    if L == m:  # 시작위치로부터 m개 채취 확인 완료
        res = max(res, 수익)
    else:
        DFS(L + 1, x, y + 1, sum_data + g[x][y], 수익 + g[x][y] ** 2)  # 이번 꿀통 채취함.
        DFS(L + 1, x, y + 1, sum_data, 수익)  # 이번 꿀통 채취 안함


T = int(input())
for t in range(1, T + 1):
    n, m, c = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    # 1. 첫번째 사람부터 선택
    res = 0
    resA = 0
    resB = 0
    최종수익 = 0
    for i in range(n):
        for j in range(n - m + 1):  # n-m까지는 벌통을 선택하는 시작위치로 가능
            # (i,j)부터 m개의 벌통 선택. 그중 최대값 갱신하고 2번쨰 사람 선택 가능
            res = 0
            DFS(0, i, j, 0, 0)
            resA = res # 미리 기억시키고
            # 2. 첫번째 사람 선택한 위치부터 두번째 사람 선택 가능
            for i2 in range(i, n):
                y = 0
                if i2 == i: # 같은 행에서 가능한 경우 따져야함.
                    y = j + m  # 첫번째 일꾼 바로 다음부터 가능
                for j2 in range(y, n - m + 1):
                    res = 0
                    DFS(0,i2,j2,0,0)
                    resB = res
                    최종수익 = max(최종수익, resA + resB)
    # 각 경우마다 따졌어야 하므로 resA = max(resA,res) resB = max(resB,res)가 아니라
    # 각 경우로서 진행했어야 했다.
    # resA = res, resB = res, 로 받아온 후 그 합이 최대인 경우만 갱신했어야했음.
    print(f"#{t} {최종수익}")