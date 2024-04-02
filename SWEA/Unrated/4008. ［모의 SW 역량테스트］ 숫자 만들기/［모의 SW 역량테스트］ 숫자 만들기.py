
def cal(val1, val2, op):
    if op == "+":
        return val1 + val2
    elif op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "/":
        return int(val1 / val2)

def DFS(L, value):
    global max_value, min_value
    if L == n-1: # n-1이 됐다는건 n-1개의 연산자를 모두 확인했음
        max_value = max(max_value, value)
        min_value = min(min_value, value)
    else: # 그게 아니라면 현재 값과 연산 진행
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                res_value = cal(value, data[L+1], operator[i])
                DFS(L+1, res_value)
                oper[i] += 1

operator = ["+", "-", "*", "/"]
T = int(input())
for t in range(1,T+1):
    n = int(input())
    oper = list(map(int, input().split())) # 연산자 각 개수 + - * / 개수 순
    data = list(map(int, input().split())) # 계산에 사용되는 숫자 oper 개수 + 1
    # 첫 숫자부터 계산 시작.
    max_value = -int(1e9)
    min_value = int(1e9)
    DFS(0,data[0])
    # print(f"max_value = {max_value}")
    # print(f"min_value = {min_value}")
    print(f"#{t} {max_value-min_value}")

