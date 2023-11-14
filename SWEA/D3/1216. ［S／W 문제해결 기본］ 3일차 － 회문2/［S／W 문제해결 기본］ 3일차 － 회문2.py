def palindrome_row(data): # 가로 최대 길이 찾는 회문
    cnt = 0
    for length in range(100, 0, -1):
        for i in range(100):
            for j in range(100):
                if j + length > 100: # 범위를 넘어가면 탈출
                    break
                e = j + length -1 # 마지막 인덱스
                for k in range(j, j + length // 2):
                    if data[i][k] != data[i][e]:
                        break
                    e -= 1
                else: # 모두 돌았어 그러면 회문
                    cnt = length
                    return cnt

def palindrome_col(data): # 세로 최대 길이 찾는 회문
    cnt = 0
    for length in range(100,0,-1):
        for i in range(100):
            for j in range(100):
                if j + length > 100: # 범위 넘으면 탈출
                    break
                e = j + length -1 # 마지막 인덱스
                for k in range(j, j+length // 2):
                    if data[k][i] != data[e][i]:
                        break
                    e -= 1
                else:
                    cnt = length
                    return cnt



T = 10
for t in range(1,T+1):
    n = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    cnt1 = palindrome_row(data)
    cnt2 = palindrome_col(data)
    cnt = max(cnt1, cnt2)

    print(f"#{t} {cnt}")