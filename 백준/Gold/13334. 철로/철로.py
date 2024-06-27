import heapq

# 철로. 집과 사무실 통근하는 n명의 사람들 존재
# 각 사람의 집과 사무실은 수평선 상에 있는 서로 다른 점에 위치
# 두 사람 A,B에 대해서 A의 집 혹은 사무실의 위치가 B의 집 혹은 사무실의 위치와 같을 수 있다.
# 철로의 길이 d로 정해져있음.
# 집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록 철로 선분 정하고자 함.
# 집과 사무실의 위치가 모두 L에 포함되는 사람들의 최대수. 시작점 끝점 모두 포함되어야 함.
# N^2 안됨

# 계속 최대인 경우를 확인하면서 진행 ?
# 시작점이 우선. 시작점 + d에 끝점이 포함이 되는지
# 안되면

n = int(input())
data = []
for _ in range(n):
    a,b = map(int, input().split())
    c = min(a,b)
    d = max(a,b)
    data.append((c,d))
d = int(input()) # 철로의 길이
cnt = 0
data.sort(key = lambda x : (x[1], x[0])) # 끝점 오름차순, 시작점 오름차순
# print(*data)
res = 0
heap = []
L = data[0][0] # 철로의 시작점 미리 설정ㄱ
# 한개씩 확인하기
for i in range(n):
    s,e = data[i] # 현재 사람의 시작시작, 끝시작
    length = e-s
    if length > d: continue # 애초에 범위 벗어나면 탈출
    heapq.heappush(heap, (s,e)) # 가능한 경우니까 일단 넣어두고
    # 불가능한 경우를 제외시키기
    if e > L+d: # 범위 초과
        while heap and heap[0][0] + d < e:
            heapq.heappop(heap)
    L = heap[0][0] # 새로 갱신
    res = max(res, len(heap))

print(res)