import sys

# sys.stdin = open("input.text", "rt")

data = list(map(int, input()))
count = 0

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count +=1
#count에는 변화횟수 저장.
#어떻게 저장되든 0으로 변한횟수와 1로 변환횟수가 한번밖에 차이가 안날꺼잖아
#(그래야 변화를 하고 "연결"을 생각)
#그러므로 더 적은 횟수가 바로 최소 횟수이다.

res = (count + 1) // 2 #1을 더해주는 이유
#0 1 0 인 경우 변화횟수 2번 뒤집는 횟수 1번
#0 1 0 1 인 경우 변화횟수 3번 뒤집는 횟수 2번. 원하는 몫을 얻기 위해!!

print(res)