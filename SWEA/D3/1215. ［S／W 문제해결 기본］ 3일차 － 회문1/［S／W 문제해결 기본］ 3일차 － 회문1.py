

def palindrome(length, data):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if j + length > 8:
                break
            # 가로
            tmp = data[i][j:j+length]
            if tmp == tmp[::-1]:
                cnt += 1
            # 세로
            temp = []
            for k in range(length):
                temp.append(data[j+k][i])
            if temp == temp[::-1]:
                cnt += 1
    return cnt


T = 10
for t in range(1,T+1):
    length = int(input()) # 찾아야 하는 회문의 길이
    data = [list(input()) for _ in range(8)]
    # 회문 찾기
    cnt = palindrome(length, data)
    print(f"#{t} {cnt}")

