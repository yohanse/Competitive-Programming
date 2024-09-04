class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        prefix_sum = [[0 for i in range(m)] for j in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j] = int(matrix[i][j]) + prefix_sum[i][j]
        
        result = 0
        for r1 in range(n):
            for r2 in range(r1, n):
                count = 0
                for c in range(m):
                    value = prefix_sum[r2 + 1][c] - prefix_sum[r1][c]
                    if value == r2 - r1 + 1:
                        count += 1
                    else:
                        count = 0
                    result = max(result, count*(r2 - r1 + 1))
        return result


