import sys


n = int(input())

# 단어 n 개 입력 받아 그룹 단어의 개수 출력하기
# 현재 순번으로부터 이전에도 존재하는지 확인해야해.
cnt = 0
for _ in range(n):
    data = input()
    temp = set()
    last = ""
    for x in data:    # 전체를 돌면서
        if x in temp and last != x:  # temp에 존재하면서 이전 값과도 같지 않다면
            break #그룹 문자 아니야
        else:  #그게 아니면 아직 가능성 존재. 추가
            temp.add(x)
        last = x
    else:
        cnt += 1

print(cnt)



