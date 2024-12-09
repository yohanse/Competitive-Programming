class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        for row in range(1, rows):
            left_to_right = [-inf for i in range(cols)]
            right_to_left = [-inf for i in range(cols)]

            prev = -inf
            for col in range(cols):
                left_to_right[col] = max(prev, points[row - 1][col] + col)
                prev = max(prev, left_to_right[col])

            prev = -inf
            for col in range(cols - 1, -1, -1):
                right_to_left[col] = max(prev, points[row - 1][col] - col)
                prev = max(prev, right_to_left[col])

            for col in range(cols):
                points[row][col] += max(left_to_right[col] - col, right_to_left[col] + col)
       
        return max(points[-1])