import sys

input = sys.stdin.readline

data = set()

m = int(input())
for _ in range(m):
    temp = list(input().split())
    oper = temp[0]
    if temp[0] != "all" and temp[0] != "empty":
        num = int(temp[1])
    if oper == "add":
        data.add(num)
    elif oper == "check":
        if num in data:
            print(1)
        else:
            print(0)
    elif oper == "remove":
        if num in data:
            data.remove(num)
    elif oper == "toggle":
        if num in data:
            data.remove(num)
        else:
            data.add(num)
    elif oper == "all":
        data = set(range(1,21))
    elif oper == "empty":
        data = set()








