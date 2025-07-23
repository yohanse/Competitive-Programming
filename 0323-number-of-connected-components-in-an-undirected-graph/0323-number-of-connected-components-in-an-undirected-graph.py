class Solution:
    def dfs(self, vertex):
        self.visited.add(vertex)
        for adjvertex in self.graph[vertex]:
            if adjvertex not in self.visited:
                self.dfs(adjvertex)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [[] for _ in range(n)]
        self.visited = set()
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        count = 0
        for vertex in range(n):
            if vertex not in self.visited:
                count += 1
                self.dfs(vertex)
        return count

        