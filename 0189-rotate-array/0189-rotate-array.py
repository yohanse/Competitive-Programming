class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # index_after_rotation = (index + k)%n
        # 0, 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 4, 5, 6, 7  k = 3, n = 7
        # temp = 2
        # _, _, 7, 1, _, _, 4
        # index              index_after_rotation
        #   0                     3
        #   3                     6
        #   6                     2

        n = len(nums)
        k %= n
        count = 0
        for index in range(k):
            start_index = index
            next_index = (start_index + k)%n
            previous = nums[start_index]
            count += 1
            while start_index != next_index:
                curr = nums[next_index]
                nums[next_index] = previous
                next_index = (next_index + k)%n
                previous = curr
                count += 1
            nums[next_index] = previous

            if count == n:
                return
          


        
                





        
        