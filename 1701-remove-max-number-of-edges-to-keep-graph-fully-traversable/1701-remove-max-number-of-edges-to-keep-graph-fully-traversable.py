class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.n = n
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u != parent_v:
            if self.rank[parent_u] == self.rank[parent_v]:
                self.rank[parent_u] += 1

            if self.rank[parent_u] > self.rank[parent_v]:
                self.parent[parent_v] = parent_u
            else:
                self.parent[parent_u] = parent_v
    
    def find(self, u):
        if u == self.parent[u]:
            return u
        
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

    def all_connected(self):
        parent = self.find(0)
        for i in range(1, self.n):
            if self.find(i) != parent:
                return False
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_disjoint_set = DisjointSet(n)
        bob_disjoint_set = DisjointSet(n)

        edges.sort(key=lambda x: -x[0])

        removed_edges = 0
        for typ, u, v in edges:
            u, v = u - 1, v - 1
            is_alice_connected = alice_disjoint_set.is_connected(u, v)
            is_bob_connected = bob_disjoint_set.is_connected(u, v)

            is_edge_used = False

            if typ != 1 and is_alice_connected == False:
                alice_disjoint_set.union(u, v)
                is_edge_used = True
            
            if typ != 2 and is_bob_connected == False:
                bob_disjoint_set.union(u, v)
                is_edge_used = True
            
            if not is_edge_used:
                removed_edges += 1
        if alice_disjoint_set.all_connected() and bob_disjoint_set.all_connected():
            return removed_edges
        return -1

        