
# 활주로 건설
# nxn, 각 보드 값은 그 지형의 높이
# 가로 또는 세로로 직선방향으로 건설할 수 있는지 확인

# 활주로는 높이가 동일한 구간에서 건설이 가능
# 경사로 길이 x, 높이 1
# 경사로는 높이차이 1이고 낮은 지형의 높가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 가능

# 동일한 셀에 두 개이상의 경사로 겹치기 X -> 한 셀마다 딱 한번 가능

T = int(input())
for t in range(1,T+1):
    n,x = map(int, input().split()) # nxn, 경사로 길이 x
    g = [list(map(int, input().split())) for _ in range(n)]

    # 열 먼저 확인
    res = 0
    for i in range(n):
        cnt = 1 # 본인 좌표 유효값 시작은 1이어야지
        for j in range(n-1):
            if g[i][j] == g[i][j+1]: # 평지 -> 유효값  +1
                cnt += 1
            elif g[i][j] + 1 == g[i][j+1]: # 오르막 만남
                if cnt >= x: #  경사로 건설 가능
                    cnt = 1 # 오르막 만났으니 초기화 -> 초기화도 본인 좌표 역시 유효하도록 1로 초기화
                else:
                    break # 안되는 경우
            elif g[i][j] == g[i][j+1] + 1: # 내리막 만남
                if cnt < 0: # 경사로 겹침 안됨
                    break
                else: # 일단 값을 대여해줌
                    cnt = -(x-1) # 현재 칸 제외 경사로 유효값을 미리 줌
            else: # 차이가 1보다 크면 경사로 놓을 수 없음 -> 그냥 안됨
                break
        else: # 반복문을 다 돌았을 때 cnt 값이 0 이상이어야만 한다
            if cnt >= 0:
                res += 1

    # 행 확인
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if g[i][j] == g[i+1][j]: # 평지
                cnt += 1
            elif g[i][j] + 1 == g[i+1][j]: # 오르막
                if cnt >= x: # 오르막 건설 가능
                    cnt = 1 # 초기화
                else:
                    break
            elif g[i][j] == g[i+1][j] + 1: # 내리막
                if cnt < 0:
                    break
                else:
                    cnt = -(x-1) # 미리 건설했다고 가정하고 값 부여
            else: # 차이가 1보다 크면 그냥 안됨
                break
        else: # 반복문 다 돈 경우만 확인
            if cnt >= 0:
                res += 1

    print(f"#{t} {res}")