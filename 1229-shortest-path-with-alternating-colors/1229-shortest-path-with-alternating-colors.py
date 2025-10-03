class Solution:
    def bfs(self, source, destination, graph):
        from collections import deque

        
        visited = set([(source, "B"), (source, "R")])
        queue = deque([(source, "N", 0)])
        while queue:
            vertex, prev_edge_color, num_edge = queue.popleft()
            if vertex == destination:
                return num_edge

            for adjvertex, edge_color in graph[vertex]:
                if (adjvertex, edge_color) not in visited and prev_edge_color != edge_color:
                    visited.add((adjvertex, edge_color))
                    queue.append((adjvertex, edge_color, num_edge + 1))
        return -1
            

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in redEdges:
            graph[a].append((b, "R"))
        
        for a, b in blueEdges:
            graph[a].append((b, "B"))
        
        answer = [0 for _ in range(n)]
        for destination in range(1, n):
            answer[destination] = self.bfs(0, destination, graph)
        
        return answer


