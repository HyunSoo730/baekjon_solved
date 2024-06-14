
# 보호필름. 각 셀은 특성 A 또는 특성 B
# 합격기준 K, 충격 세로 방향으로 주어짐.
# 각 열마다 동일한 특성의 셀들이 K개 이상 연속적으로 있으면 해당 열은 통과
# 성능 검사 통과하기 위해 약품 사용.
# 최소 약품 투입 횟수 구하기

def 확인(g):
    for j in range(m):
        flag = False # 해당 열 가능한지 판단.
        for i in range(n):
            cnt = 0
            end = i
            now = g[i][j]
            while end < n and now == g[end][j]:
                cnt += 1
                end += 1
                if cnt >= k and not flag:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return False
    return True


def 성능검사(L, now, g):
    global res
    if now >= res:
        return
    if 확인(g):
        res = min(res, now)
    else: # 조합. 약품 사용.
        for i in range(L, n):
            for j in range(2):
                copy_g = [arr[:] for arr in g]
                for k in range(m):
                    copy_g[i][k] = j
                성능검사(i+1, now+1, copy_g)


T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    # 특성은 0 또는 1
    res = int(1e9)
    성능검사(0,0,g)
    print(f"#{t} {res}")