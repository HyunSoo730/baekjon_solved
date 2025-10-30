from collections import deque

def solution(game_board, table):
    n = len(game_board)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    def isInner(x,y):
        return 0<=x<n and 0<=y<n
    
    # 1. BFS로 연결된 영역 찾기 (빈공간이든 퍼즐이든)
    def bfs(board, x, y, target, visited):
        """
        board: 탐색할 보드
        x,y: 시작 위치
        target: 찾을 값 (0 또는 1)
        visited: 방문체크 배열
        반환: 연결된 좌표들의 리스트
        """
        dq = deque()
        dq.append((x,y))
        visited[x][y] = True
        coords = [(x,y)]  # 이 영역의 모든 좌표
        
        while dq:
            cx, cy = dq.popleft()
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if not isInner(nx,ny): continue
                if visited[nx][ny]: continue
                if board[nx][ny] != target: continue
                
                visited[nx][ny] = True
                dq.append((nx,ny))
                coords.append((nx,ny))
        
        return coords
    
    # 2. 좌표들을 (0,0) 기준으로 정규화
    def normalize(coords):
        """
        예: [(2,3), (2,4), (3,3)] -> [(0,0), (0,1), (1,0)]
        """
        min_x = min(x for x,y in coords)
        min_y = min(y for x,y in coords)
        
        normalized = []
        for x,y in coords:
            normalized.append((x - min_x, y - min_y))
        
        normalized.sort()  # 비교를 위해 정렬
        return normalized
    
    # 3. 도형 회전 (90도씩)
    def rotate(coords):
        """
        (x,y) -> (y, -x) : 90도 시계방향 회전
        """
        rotated = []
        for x,y in coords:
            rotated.append((y, -x))
        
        return normalize(rotated)  # 회전 후 다시 정규화
    
    # 4. 모든 빈공간 찾기
    visited_board = [[False] * n for _ in range(n)]
    empty_spaces = []
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited_board[i][j]:
                coords = bfs(game_board, i, j, 0, visited_board)
                empty_spaces.append(normalize(coords))
    
    # 5. 모든 퍼즐조각 찾기
    visited_table = [[False] * n for _ in range(n)]
    puzzle_pieces = []
    
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited_table[i][j]:
                coords = bfs(table, i, j, 1, visited_table)
                puzzle_pieces.append(normalize(coords))
    
    # 6. 매칭하기
    used = [False] * len(puzzle_pieces)  # 퍼즐 사용 여부
    answer = 0
    
    for empty in empty_spaces:
        for idx, piece in enumerate(puzzle_pieces):
            if used[idx]: continue  # 이미 사용한 퍼즐
            
            # 퍼즐을 0도, 90도, 180도, 270도 회전시켜보기
            current = piece
            matched = False
            
            for _ in range(4):  # 4번 회전
                if empty == current:  # 빈공간과 퍼즐이 일치!
                    used[idx] = True
                    answer += len(empty)  # 채운 칸 수 추가
                    matched = True
                    break
                
                current = rotate(current)  # 90도 회전
            
            if matched:
                break  # 이 빈공간은 채웠으니 다음 빈공간으로
    
    return answer