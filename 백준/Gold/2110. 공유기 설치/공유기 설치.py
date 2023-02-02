import sys

N, C = map(int ,input().split())
data = []

for _ in range(N):
    data.append(int(input()))

data.sort()

#값의 범위가 정해져있음
start =1
end = max(data) -1

def countLen(len):
    cnt = 1 #시작할 때 박고 시작
    now = data[0] #현재 박힌 위치 now
    for i in range(1, N):
        if data[i] - now >= len:
            cnt += 1
            now = data[i]
    
    return cnt

res = -2424242424 #최대 거리
while start <= end:
    mid = (start + end) // 2 #인접한 두 공유기 사이의 최대 거리 이 거리보단 같거나 커야 설치가능

    if countLen(mid) >= C: #거리가 작으면 작을 수록 더 설치하므로 어쩃든 C이상이면 답의 유효한 범위
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)

