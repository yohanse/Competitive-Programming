class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        nodes_leng = len(values)
        graph = [[] for i in range(nodes_leng)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def postorder(parent, vertex):
            if vertex != 0 and len(graph[vertex]) == 1:
                return values[vertex]
            
            sumii = 0
            for adjvertex in graph[vertex]:
                if adjvertex != parent:
                    sumii += postorder(vertex, adjvertex)
            return min(sumii, values[vertex])

        return sum(values) - postorder(-1,0)