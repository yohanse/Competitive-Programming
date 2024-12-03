class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        nodes_leng = len(values)
        graph = [[] for i in range(nodes_leng)]
        incoming = [0 for i in range(nodes_leng)]
        dp = [inf for i in range(nodes_leng)]
        sumii = [0 for i in range(nodes_leng)]

        for a, b in edges:
            incoming[a] += 1
            incoming[b] += 1

            graph[a].append(b)
            graph[b].append(a)
        
        incoming[0] += 1
        
        stack = []
        for node in range(nodes_leng):
            if incoming[node] == 1:
                sumii[node] = values[node]
                stack.append(node)
            
        while stack:
            vertex = stack.pop()
            dp[vertex] = min(sumii[vertex], values[vertex])
            for adjvertex in graph[vertex]:
                if incoming[adjvertex] != 0:
                    sumii[adjvertex] += dp[vertex]
                    incoming[adjvertex] -= 1
                    if incoming[adjvertex] == 1:
                        stack.append(adjvertex)

        return sum(values) - dp[0]

        
        
        