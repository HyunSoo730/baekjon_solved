
T = 10
for i in range(T):
    n = int(input()) # 덤프 횟수
    data = list(map(int, input().split()))
    for _ in range(n):
        max_idx = data.index(max(data))
        min_idx = data.index(min(data))
        data[max_idx] -= 1
        data[min_idx] += 1
    print(f"#{i+1} {max(data) - min(data)}")
    
