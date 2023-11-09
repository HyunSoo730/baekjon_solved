

T = int(input())
for t in range(T):
    data = list(map(int, input()))
    # 오른쪽에서부터 카운트
    cnt = 0
    n = len(data)
    idx = n-1
    while True:
        x = data[idx]
        for i in range(idx, -1, -1):
            if data[idx] != data[i]:
                idx = i
                break
        else:
            if x == 1:
                cnt += 1
                break
            else:
                break
        cnt += 1
        if x == 0:
            for i in range(idx+1, n):
                data[i] = 1
        else:
            for i in range(idx+1, n):
                data[i] = 0
    print(f"#{t+1} {cnt}")