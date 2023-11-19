import sys

n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수들


# 이 중에서 n-1개의 oper 선택해서 삽입.
max_data = -int(1e9)
min_data = int(1e9)
def dfs(L, sum, add, sub, mul, div):
    global max_data
    global min_data
    if L == n - 1:  # 모든 연산자 확인
        max_data = max(max_data, sum)
        min_data = min(min_data, sum)
    else:
        if add > 0:  # 연산 진행 가능
            dfs(L + 1, sum + data[L + 1], add - 1, sub, mul, div)
        if sub > 0:
            dfs(L + 1, sum - data[L + 1], add, sub - 1, mul, div)
        if mul > 0:
            dfs(L + 1, sum * data[L + 1], add, sub, mul - 1, div)
        if div > 0:
            dfs(L + 1, int(sum / data[L + 1]), add, sub, mul, div - 1)
dfs(0,data[0], oper[0], oper[1], oper[2], oper[3])
print(max_data)
print(min_data)