# 素集合データ構造
parent = [i for i in range(N)]
rank = [0 for i in range(N)]
 
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
 
def union(a, b):
    rootA = find(a)
    rootB = find(b)
 
    if rootA == rootB:
        return
    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA
        if rank[rootA] == rank[rootB]:
            rank[rootA] += 1