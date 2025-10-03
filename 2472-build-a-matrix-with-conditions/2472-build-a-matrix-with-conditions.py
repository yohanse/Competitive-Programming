class Solution:
    def topological_sort_order(self, vertex, color, graph, order):
        if color[vertex] == 1:
            return False, []
        
        
        color[vertex] = 1
        for adjvertex in graph[vertex]:
            if color[adjvertex] != 2:
                if not self.topological_sort_order(adjvertex, color, graph, order)[0]:
                    return False, []
        order.append(vertex)
        color[vertex] = 2
        return True, order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = [[] for _ in range(k)]
        row_color = [0 for _ in range(k)]
        row_order = []

        col_graph = [[] for _ in range(k)]
        col_color = [0 for _ in range(k)]
        col_order = []

        for u, v in rowConditions:
            row_graph[v - 1].append(u - 1)

        for u, v in colConditions:
            col_graph[v - 1].append(u - 1)
        
        for i in range(k):
            if row_color[i] == 0:
                is_topo, order = self.topological_sort_order(i, row_color, row_graph, [])
                
                if not is_topo:
                    return []
                
                for v in order:
                    row_order.append(v)
        
        for i in range(k):
            if col_color[i] == 0:
                is_topo, order = self.topological_sort_order(i, col_color, col_graph, [])
                if not is_topo:
                    return []
                
                for v in order:
                    col_order.append(v)
        
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if row_order[i] == col_order[j]:
                    matrix[i][j] = 1 + row_order[i]
        return matrix
        
        