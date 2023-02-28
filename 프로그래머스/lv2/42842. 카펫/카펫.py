def solution(brown, yellow):
    a = brown
    b = yellow
    
    #a+b = xy 이용
    n = a+b #가로 세로 넓이.
    cnt = 0
    res = []
    for y in range(1,n+1): #세로를 통해서 ?
        #n/x = y
        if n % y == 0:
            x = n // y
        if x*y == n:
            if x >= y and (x-2) * (y-2) == b:
                resX = x
                resY = y
                
    res.append(resX)
    res.append(resY)
    return res