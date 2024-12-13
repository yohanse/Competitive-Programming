class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        unique_numbers = 10
        rows, cols = len(grid), len(grid[0])

        occurence = [[0 for i in range(unique_numbers)] for j in range(cols)]
        dp = [[0 for i in range(unique_numbers)] for j in range(cols + 1)]

        # counting the occurence of each number by each column
        for row in range(rows):
            for col in range(cols):
                occurence[col][grid[row][col]] += 1
        
        for col in range(cols):
            for num in range(unique_numbers):
                dp[col + 1][num] = self.minimum_except_num(dp[col], num, unique_numbers) + rows - occurence[col][num]
                
        return min(dp[-1])

    def minimum_except_num(self, array, num, unique_numbers):
        ans = inf
        for i in range(unique_numbers):
            if i != num:
                ans = min(ans, array[i])
        return ans
