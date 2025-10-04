class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_childrens = len(ratings)
        min_candy = 0

        left_right = [1 for _ in range(num_childrens)]
        right_left = [1 for _ in range(num_childrens)]

        for i in range(1, num_childrens):
            if ratings[i] > ratings[i - 1]:
                left_right[i] = left_right[i - 1] + 1
        
        for i in range(num_childrens - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_left[i] = right_left[i + 1] + 1
        
        for i in range(num_childrens):
            min_candy += max(right_left[i], left_right[i])
        
        return min_candy