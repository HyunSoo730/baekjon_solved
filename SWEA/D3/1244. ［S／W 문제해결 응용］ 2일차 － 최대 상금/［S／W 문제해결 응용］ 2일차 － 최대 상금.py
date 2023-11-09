
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    data, K = input().split()
    K = int(K)
    N = len(data)
    # 중복을 제거한 경우의 수를 담아주기 위한 set
    now = set([data])
    nxt = set()

    # 교환만큼 반복
    for _ in range(K):
        # now 빌 때까지
        while now:
            s = now.pop()
            # 리스트로 변환
            s = list(s)
            # 가능한 모든 경우의 수를 nxt에 담는다
            # set 자료구조 특성상 중복 제외됨.
            for i in range(N):
                for j in range(i + 1, N):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    # 원상 복구
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print('#{} {}'.format(tc, max(map(int, now))))