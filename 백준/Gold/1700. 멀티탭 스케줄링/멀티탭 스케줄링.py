import sys
import heapq

# 멀티탭. 플러그를 빼는 횟수를 최소화 하는 방법.
n,k = map(int, input().split())
data = list(map(int, input().split()))

"""
멀티탭 N개 (한정된 자원)
- K개 순서대로 사용.
- 플러그 빼는 횟수 최소화
콘센트 꽉 찼을 때 어떤 플러그를 뽑아야 하는가.

최적 전략 : 가장 나중에 다시 사용될 플러그를 뽑는다.
이유 :
- 곧 사용할 것 뽑으면 -> 바로 다시 꽂아야함
- 늦게 사용할 것 뽑으면 -> 오래 비워둘 수 있음

제거 우선순위
- 더 이상 사용하지 않는 것
- 가장 나중에 쓰는 것
"""

cnt = 0
check = set() # 이미 있는 것도 알아야지
for i in range(k):
    now = data[i] # 현재 넘버
    # Case 1. 이미 꽂혀있음
    if now in check: # 이미 존재하면
        continue
    # Case 2. 빈 자리 있음
    if len(check) < n: # 아직 덜 담겼어
        check.add(data[i]) # 계속 담을 수 있음
        continue

    # Case 3. 꽉 참 - 제거 대상 선택
    heap = [] # 힙 구성 : 다음 사용 시점, 제품 번호 가장 나중에 쓰이는 것을 뽑아야 하니 최대힙 (인덱스기반!)
    for num in check:
        # num 다음 사용 시점 찾기
        next_use = k # 기본값 : 끝 (더이상 안씀)
        for j in range(i + 1, k):
            if data[j] == num:
                next_use = j
                break

        # 최대힙을 위해 음수로
        heapq.heappush(heap, (-next_use, num))
    # 가장 나중 것 제거
    _, num = heapq.heappop(heap)
    check.remove(num)
    check.add(now)
    cnt += 1

print(cnt)
