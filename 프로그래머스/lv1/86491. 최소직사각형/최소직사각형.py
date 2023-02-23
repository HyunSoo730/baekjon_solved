#가로 세로 바꿨을 때 최대 비교?
def solution(sizes): #2차원 배열 sizes 지갑의 크기 리턴하기 (가로, 세로)
    max_x = 0
    max_y = 0
    for x,y in sizes:
        if x < y: #세로가 더 크면
            x,y = y,x
        max_x = max(max_x, x)
        max_y = max(max_y,y)
    
    return max_x * max_y
    
    
    