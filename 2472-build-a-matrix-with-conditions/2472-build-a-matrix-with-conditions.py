class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowConditions = list(set([(a, b) for a, b in rowConditions]))
        colConditions = list(set([(a, b) for a, b in colConditions]))

        incoming_row = [0 for i in range(k)]
        incoming_col = [0 for i in range(k)]
        graph_row = [[] for i in range(k)]
        graph_col = [[] for i in range(k)]

        for a, b in rowConditions:
            a, b = a - 1, b - 1
            incoming_row[b] += 1
            graph_row[a].append(b)
        
        for a, b in colConditions:
            a, b = a - 1, b - 1
            incoming_col[b] += 1
            graph_col[a].append(b)
        
        
        row = [0 for i in range(k)]
        index = 0
        for i in range(k):
            if not incoming_row[i]:
                q = deque([i])
                while q:
                    vertex = q.popleft()
                    row[vertex] = index
                    index += 1
                    for adjvertex in graph_row[vertex]:
                        incoming_row[adjvertex] -= 1
                        if not incoming_row[adjvertex]:
                            incoming_row[adjvertex] -= 1
                            q.append(adjvertex)
        if index != k:
            return []
        col = [0 for i in range(k)]
        index = 0
        for i in range(k):
            if not incoming_col[i]:
                q = deque([i])
                while q:
                    vertex = q.popleft()
                    col[vertex] = index
                    index += 1
                    for adjvertex in graph_col[vertex]:
                        incoming_col[adjvertex] -= 1
                        if not incoming_col[adjvertex]:
                            incoming_col[adjvertex] -= 1
                            q.append(adjvertex)
        if index != k:
            return []
        matrix = [[0 for i in range(k)] for i in range(k)]
        for i in range(k):
            matrix[row[i]][col[i]] = i + 1
        return matrix
