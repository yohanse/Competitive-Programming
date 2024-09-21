class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.rank[parent_a] += 1
                self.parent[parent_b] = parent_a
            else:
                self.rank[parent_b] += 1
                self.parent[parent_a] = parent_b
            return False
        return True

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    



class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)

        disjoint_1 = Disjoint(n)
        disjoint_2 = Disjoint(n)

        count = 0
        for c, b, a in edges:
            a, b = a - 1, b - 1
            
            if c == 3: 
                r1, r2 = disjoint_1.union(a, b), disjoint_2.union(a, b)
                count += (r1 and r2)

            if c == 2 and disjoint_1.union(a, b):
                count += 1

            if c == 1 and disjoint_2.union(a, b):
                count += 1 

        for i in range(n):
            disjoint_1.find(i)
            disjoint_2.find(i)
        
        if len(set(disjoint_1.parent)) != 1 or len(set(disjoint_2.parent)) != 1:
            return -1
        return count
        