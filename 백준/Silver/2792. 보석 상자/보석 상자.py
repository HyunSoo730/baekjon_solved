import sys

n,m = map(int, input().split())
data = []
for _ in range(m):
    temp = int(input())
    data.append(temp)

# 질투심 X로 모든 학생에게 나누어 줄 수 있는가 ?
left, right = 1, max(data) + 1

def is_possible(max_jewel): # 해당 최대 질투심으로 모든 학생에게 나눠줄 수 있는가
    total = 0 # 학생 수
    for cnt in data: # 각 컬러의 개수
        total += (cnt + max_jewel - 1) // max_jewel # 올림 진행 : a // b 그대로 안하고, (a+b-1) // b -> 올림
    return total <= n # 왜 n명 이하 ? n명 넘어가면 안되지 당연. 또한 n보다 이하여도 ok.


while left < right:
    mid = (left + right) // 2

    if not is_possible(mid): # 불가능 (n명에게 나눠줄 수 없음)
        left = mid + 1 # 늘려야지
    else:
        right = mid

print(left)
