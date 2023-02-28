import sys

def find_parent(x): #x노드의 부모(속하는 집합) 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b): #a,b 노드를 합치기
    a = find_parent(a)
    b = find_parent(b)
    if a < b: #b가 더 크면 b의 부모를 a로
        parent[b] = a
    else:
        parent[a] = b


r = 1
while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    parent = [0] * (n+1)
    for i in range(1,n+1):
        parent[i] = i
    temp = []
    cycle = False #사이클 판별을 위해
    for _ in range(m):
        a,b = map(int, input().split()) #a,b노드는 연결
        a = find_parent(a)
        b = find_parent(b)

        if a == b:
            cycle = True
            temp.append(a)
        else:
            union_parent(a,b)
        
        if a in temp or b in temp: #해당 집합이 사이클 집합에 포함되면 트리처리가 아니라 사이클 처리로 트리 개수에서 제외해야함.
            temp.append(a)
            temp.append(b) #두 정점 중 하나가 사이클에 포함되는 정점이라면 나저미 정점도 사이클로 포함.

        # if find_parent(a) == find_parent(b): #중복 없이 처음으로 등장하는데
        #     #부모가 같다면. 사이클 발생.
        #     cycle = True
        #     a = find_parent(a) #a,b중 아무거나 부모 인덱스 받아와서 저장.
        #     temp.append(a) #사이클이 발생한 인덱스(집합) 따로 저장. 즉 해당 집합을 따로 저장.
        # else:
        #     union_parent(a,b)
    
    check = set(temp)   #만약 사이클이 있다면 추가해야지.
    for i in range(1,n+1):
        find_parent(i) #부모 갱신 굳이 안해줘도 ?
    # print(parent)
    
    # print(check)
    cnt = 0
        
    for i in range(1,n+1):
        if parent[i] in check: #사이클이 있는 집합은 check에 추가해놓고 나중에 방문 안해야함.
            continue
        cnt += 1 #해당 집합(트리) 개수 추가
        check.add(parent[i]) #이제 해당 집합 포함시켰으니 다른 트리 찾아야지
        #check에 추가시켜서 다음에 방문 또 안하도록.
    if cnt == 0:
        print(f"Case {r}: No trees.")
    elif cnt == 1:
        print(f"Case {r}: There is one tree.")        
    else:
        print(f"Case {r}: A forest of {cnt} trees.")
    r += 1


    
