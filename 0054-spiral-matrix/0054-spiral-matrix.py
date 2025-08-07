class Solution:   
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x1, y1 = (0, 0)
        x2, y2 = (rows - 1, cols - 1)
        result = []
        while x1 <= x2 and y1 <= y2:
            for i in range(y1, y2 + 1):
                result.append(matrix[x1][i])
            
            for i in range(x1 + 1, x2 + 1):
                result.append(matrix[i][y2])

            if x1 == x2 or y2 == y1:
                return result

            for i in range(y2 - 1, y1 - 1, -1):
                result.append(matrix[x2][i])
            
            for i in range(x2 - 1, x1, -1):
                result.append(matrix[i][y1])
            
            x1, y1 = x1 + 1, y1 + 1
            x2, y2 = x2 - 1, y2 - 1
        return result


        