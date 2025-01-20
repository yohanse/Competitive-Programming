class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        subsets = []
        def rec(index, subset):
            if index == n:
                if len(subset) > 1:
                    subsets.append(subset.copy())
                return
            
            rec(index + 1, subset)
            subset.append(index)
            rec(index + 1, subset)
            subset.pop()
        rec(0, [])

        def bfs(subset, source):
            stack = [(source, 0)]
            visited = [False for i in range(n)]
            visited_subset = [False for i in range(n)]
            for ele in subset:
                visited_subset[ele] = True
            visited[source] = True
            max_dis = 0
            while stack:
                vertex, dis = stack.pop()
                if dis > max_dis:
                    source = vertex
                    max_dis = dis

                for adjvertex in graph[vertex]:
                    if not visited[adjvertex] and visited_subset[adjvertex]:
                        stack.append((adjvertex, dis + 1))
                        visited[adjvertex] = True
            return max_dis, source, visited == visited_subset
        
        result = [0 for i in range(n - 1)]
        for subset in subsets:
            dis, source, isSubset = bfs(subset, subset[0])
            if isSubset:
                dis, source, isSubset = bfs(subset, source)
                result[dis - 1] += 1
        return result
                
        
