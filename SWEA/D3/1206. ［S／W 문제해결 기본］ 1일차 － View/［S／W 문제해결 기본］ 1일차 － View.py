

def isBig(i):
    if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
        return True
    else:
        return False

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    res = 0
    for i in range(2, n - 2):
        if isBig(i):
            res += data[i] - max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
    # print(f"#{test_case} {res}")
    print("#%d %d" %(test_case, res))



