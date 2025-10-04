import sys
import heapq

# 책 총 N권 -> 번호 부여되어 있음. (1~N 번호 존재)
# 학생 M명, M명에게 신청서 a,b 받음, 책 번호 a이상 b이하인 책 중 남아있는 책 한 권 골라 해당 학생에게 줌
# 책을 줄 수 있는 최대 학생 수

# 각 학생이 적은 a~b...
"""
크기가 올라갈수록 제약 커짐 -> 후보군 감소
"""
T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    data = []
    for _ in range(m):
        a,b = map(int, input().split())
        data.append((a,b))
    # a,b 작은 순으로 해서.. 작은 값부터 채워넣자
    data.sort(key = lambda x : (x[1], x[0]))

    res = 0
    visited = [False] * (n+1)
    for a, b in data: # 각 학생에 대해서
        for num in range(a,b+1):
            if not visited[num]: # 가능한 경우
                visited[num] = True
                res += 1
                break

    print(res)

