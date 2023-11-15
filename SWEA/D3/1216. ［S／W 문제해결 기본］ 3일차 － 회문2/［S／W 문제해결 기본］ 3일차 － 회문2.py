

def palindrome_row(data): # 100x100  가로 확인
    cnt = 0
    for length in range(100, 0, -1): # 100부터 1까지 줄여나가면서 최대 찾기
        for i in range(100):
            for j in range(100):
                if j + length > 100: # 범위 벗어날 시 끝
                    break
                e = j + length -1 # 마지막 인덱스
                for k in range(j,j+length):
                    if data[i][k] != data[i][e]: # 회문이 아닐 시
                        break
                    e -= 1 # 통과할 때마다 끝 인덱스는 줄여나가야지
                else: # 반복문 모두 돈 경우 : 회문이 맞아
                    cnt = length
                    return cnt # length는 100에서 줄여나가고 있기 때문에 바로 리턴하면 돼

def palindrom_col(data): # 100x100 세로 확인
    cnt = 0
    for length in range(100,0,-1):
        for i in range(100):
            for j in range(100):
                if j + length > 100: # 범위 벗어날 시 끝
                    break
                e = j + length -1 # 역시 마지막 인덱스로 설정
                for k in range(j, j+length):
                    if data[k][i] != data[e][i]: # 회문이 아닌 경우
                        break
                    e -= 1
                else:
                    cnt = length
                    return cnt

T = 10
for t in range(1,T+1):
    n = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    res = 0
    cntA = palindrome_row(data)
    cntB = palindrom_col(data)
    res = max(cntA, cntB)
    print(f"#{t} {res}")



