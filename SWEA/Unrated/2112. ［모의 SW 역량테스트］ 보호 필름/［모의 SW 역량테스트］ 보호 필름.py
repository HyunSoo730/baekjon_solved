
# 보호필름 세로 D, 가로 W 크기
# 각 셀은 특성 A , B 둘 중 하나 특성 A는 0으로, B는 1로 표시
# 보호 필름의 성능 검사하기 위해 합격 기준 K
# 단면의 모든 세로 방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사 통과
# 즉 각 열 별로 동일한 특성이 K개 이상 있는지 판단

# 성능 검사 통과를 위해 약품 사용
# 약품은 사용한 행에 모든 특성을 하나로 변경 즉 특정 행 특성을 A 또는 B로 다 변경 가능

# 구하고자 : 약품 투입횟수 최소로 하면서 성능검사 통과할 수 있는 방법. 이때의 약품 투입 횟수
# -> 전부 다 해봐야함. 완탐 -> 근데 하나씩 다 해보면서 진행. 안될 때 그 이전 시점으로 돌아와서 다시 실행
# DFS로 진행해야 한다

def check(g): # 현재 보드 통과하는지
    for j in range(m):
        flag = False # 해당 열이 가능한지
        for start in range(n): # 열 고정, 행 내려가면서 검사
            cnt = 0
            end = start
            while end < n and g[end][j] == g[start][j]:
                cnt += 1
                end += 1 # 한칸씩 전진
            if not flag and cnt >= k: # 해당 열은 통과
                flag = True
                break # 해당 열은 가능하니까 바로 끝
        if not flag: # 현재 보드 통과 못함
            return False
    else:
        return True # 전체 다 돌았다는 건 가능하다.

def DFS(start, L, g): # 보드는 계속 가지고 다녀야함
    global res
    if L >= res: return  # 가지치기
    if check(g): # 가능하다
        res = min(res, L)
    else: # 안된다면 이제 약품 투입
        for x in range(start, n): # start행부터 n-1행까지 특정 행 선택해서. 조합인 이유는 위에서 설명
            for i in range(2): # 특성 A, B둘 다 해봐야
                copy_g = [arr[:] for arr in g]
                for y in range(m):
                    copy_g[x][y] = i
                DFS(x+1, L+1, copy_g)
                # 백트랙킹 시 원상복구는 반복문 돌면 다시 배열복사 하기 떄문에 안해도 된다.


T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split()) # 필름 크기, 합격기준 k
    g = [list(map(int, input().split())) for _ in range(n)]
    res = int(1e9)
    DFS(0,0,g)

    print(f"#{t} {res}")
