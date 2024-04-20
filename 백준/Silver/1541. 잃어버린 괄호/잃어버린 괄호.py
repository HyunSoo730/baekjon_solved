import sys

# 양수와 +,- 그리고 괄호를 가지고 식을 만들기
# 그리고 괄호 모두 지우기
# - 부호를 기준으로 분리

oper = input()
# print(data)
res = 0
num = 0
stack = []
data = []
for x in oper:
    if x == "-" or x == "+": # 연산자
        data.append(num)
        num = 0 # 초기화
        stack.append(x)
    else:
        num = num * 10 + int(x)
else: # 끝까지 돌면 결국 숫자라서
    data.append(num)

res = 0
now = data.pop()
while stack:
    oper = stack.pop() # 연산자 꺼내서
    num = data.pop() # 마지막 값 꺼내서
    if oper == "+":
        now += num
    else: # 음수면 이제 전환
        res -= now
        now = num # 마지막으로 뽑은 거 기억
else:
    res += now # 마지막에 더해주기
print(res)