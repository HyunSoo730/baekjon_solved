import sys


N, L = map(int, input().split())
data = list(map(int ,input().split()))

#물이 새는 위치 오름차순 정렬
data.sort()

start = data[0] - 0.5  #테이프 붙이는 처음 시점
end = start  + L #길이가 L이라서.
count = 1
#테이프가 끝나는 곳 start + L : end
#물이 새는 위치 순회하면서 start보다 크고 end보다 작은 값은 넘어가고 cnt + 1하면서 구하면 되겠다.

for x in data[1:]:
    if start < x < end:
        continue
    else:
        count += 1
        start = x- 0.5
        end = start + L

print(count)
