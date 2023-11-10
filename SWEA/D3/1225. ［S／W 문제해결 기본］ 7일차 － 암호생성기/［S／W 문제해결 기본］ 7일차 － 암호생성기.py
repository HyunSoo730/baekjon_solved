
from collections import deque

def cycle(dq):
    while True:
        for i in range(1,6):   # 사이클
            now = dq.popleft()
            if now - i <= 0:
                dq.append(0)
                return dq
            dq.append(now - i)


T = 10
for t in range(1,T+1):
    test_case = int(input())
    data = list(map(int, input().split()))
    dq = deque(data)
    res = cycle(dq)
    print(f"#{t}", end = " ")
    print(*res)

