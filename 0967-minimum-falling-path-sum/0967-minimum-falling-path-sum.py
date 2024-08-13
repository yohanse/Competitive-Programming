class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(1, n):
            for c in range(n):
                min_result = matrix[r - 1][c]

                if c != n - 1:
                    min_result = min(min_result, matrix[r - 1][c + 1])
                
                if c != 0:
                    min_result = min(min_result, matrix[r - 1][c - 1])

                matrix[r][c] += min_result
        
        return min(matrix[-1])