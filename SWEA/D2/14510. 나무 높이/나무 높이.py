
# n개의 나무
# 각 나무는 키가 존재
# 홀수는 1, 짝수는 2

def solve():
    max_height = max(data)
    # 각 나무가 자라야 할 높이 게산
    even = odd = 0
    for height in data: # 높이 하나씩 꺼내서
        diff = max_height - height # 최대높이 - 현재 높이
        even += diff // 2 # 2만큼 자라야 하는 횟수
        odd += diff % 2 # 1만큼 자라야 하는 횟수
    # 규칙에 따라 최소 일수 계산
    if even > odd: # 2가 더 크면 차이를 1로 만들어주기
        while abs(even-odd) > 1:
            even -= 1
            odd += 2 # 2일을 1일 2개로 만들기
    if odd > even: # 그냥 1의 개수만큼
        return 2 * odd -1
    elif even > odd:
        return 2 * even # 2의 개수만큼 -> 차이 1로 만들어줬기 때문.
    else:
        return odd + even # 1,2개수 동일하면 더한 값


T = int(input())
for t in range(1,T+1):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort(reverse = True)
    MAX = data[0]
    days = [0] * n
    for i in range(n):
        days[i] = MAX - data[i]
    res = solve()
    print(f"#{t} {res}")


    # 가능한 경우. days에 남아있는 날짜가 1로 나눠떨어진다 2로 나눠떨어진다.
    # 그 중에서 1이 더 많다, 2가 더 많다, 1,2 같다
    # 나눠서 생각

