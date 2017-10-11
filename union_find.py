class UnionFind:
    def __init__(self, _n):
        # 素集合データ構造
        self.parent = [i for i in range(_n)]
        self.rank = [0 for _ in range(_n)]

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]    

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            if self.rank[rootA] == self.rank[rootB]:
                self.rank[rootA] += 1

if __name__ == '__main__':
    u = UnionFind(5)
    u.union(2, 4)
    u.union(1, 3)
    u.union(2, 3)
    print(u.parent)
    print(u.rank)
