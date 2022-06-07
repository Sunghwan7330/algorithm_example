
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    v, e = map(int, input().split())
    
    parent = [0] * (v+1)
    for i in range(1, v+1):
        parent[i] = i
    
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append([c, a, b])
    
    edges.sort()
    last = 0

    result = 0
    for cost, a, b in edges:
         if find_parent(parent, a) != find_parent(parent, b):
             union_parent(parent, a, b)
             result += cost
             last = cost
    
    print(result - last)

solution()