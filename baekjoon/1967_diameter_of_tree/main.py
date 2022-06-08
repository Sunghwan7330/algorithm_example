from collections import deque

def get_max_distancee_bfs(nodes, n, pos):
    queue = deque()

    cost = 0
    queue.append((pos, 0))
    max_cost = 0
    max_idx = pos
    chear_arr = [0] * (n+1)
    
    while queue:
        p, cost = queue.popleft()
        chear_arr[p] = 1
        if cost > max_cost:
            max_cost = cost
            max_idx = p

        for node in nodes[p]:
            np, co = node
            if chear_arr[np] == 1 : continue

            queue.append((np, co + cost))
            

    return max_idx, max_cost

def solution():
    n = int(input())
    
    nodes = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, cost = list(map(int, input().split()))
        nodes[a].append([b, cost])
        nodes[b].append([a, cost])

    max_idx, max_cost = get_max_distancee_bfs(nodes, n, 1)
    max_idx, max_cost = get_max_distancee_bfs(nodes, n, max_idx)

    print(max_cost)

    
solution()
