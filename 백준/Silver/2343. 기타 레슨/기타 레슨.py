import sys

# 총 N개의 강의. 순서 바뀌면 안됨.
# M개의 블루레이에 모든 동영상 녹화 예정.
# 블루레이의 크기(녹화 가능한 길이)를 최소로. (M개의 블루레이는 모두 같은 크기)
# 즉.. M개의 블루에이에 모든 동영상을 녹하하되, 블루레이 크기 가능한 최소...
# -> 결정 문제 (특정 조건하 최솟값)
# 녹화 가능한 길이 증가할수록 블루레이 개수 감소

n,m = map(int, input().split())
data = list(map(int, input().split()))
# 녹화 가능한 길이를 변수로
left, right = max(data), sum(data) + 1

def is_possible(length):
    cnt = 1 # 사용한 블루레이 개수 : 시작 1
    total_length = data[0]
    for i in range(1,n):
        if total_length + data[i] > length: # 녹화 가능한 길이 넘어가면 이제 추가
            cnt += 1
            total_length = data[i]
        else:
            total_length += data[i]
    return cnt <= m # m개 가능 m개 안에 모두 담아야 하므로, m개 이하도 가능.


while left < right:
    mid = (left + right) // 2 # 녹화 가능한 길이.
    if not is_possible(mid): # 불가능하다면 : M개 안에 못만들어.
        left = mid + 1 # 그렇다면 길이를 늘려서 해봐야지.
    else:
        right = mid

print(left)

