def solution(sizes):
    max_x = 0
    max_y = 0
    data = sizes
    for x,y in sizes:
        a = max(x,y)
        b = min(x,y)
        max_x = max(max_x, a)
        max_y = max(max_y, b)
    
    return max_x * max_y
        