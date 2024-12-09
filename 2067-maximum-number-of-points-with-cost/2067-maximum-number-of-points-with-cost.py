class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        for row in range(1, rows):
            left_to_right = [-inf for i in range(cols + 1)]
            right_to_left = [-inf for i in range(cols + 1)]

            for col in range(cols):
                left_to_right[col + 1] = max(left_to_right[col], points[row - 1][col] + col)

            for col in range(cols - 1, -1, -1):
                right_to_left[col] = max(right_to_left[col + 1], points[row - 1][col] - col)
            
            for col in range(cols):
                points[row][col] += max(left_to_right[col + 1] - col, right_to_left[col] + col)
       
        return max(points[-1])