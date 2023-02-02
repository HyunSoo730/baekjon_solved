import sys
input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))


limit.sort(reverse = True)
data.sort(reverse = True)
res = 0

if limit[0] < data[0]:
    print(-1)
else:
    while len(data) > 0:
        for crane in limit:
            for i in range(len(data)):
                if crane >= data[i]:
                    data.pop(i)
                    break
        res += 1
    
    print(res)


        