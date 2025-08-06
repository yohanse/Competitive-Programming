class Solution:
    def find_pivot(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                return i
        return -1
    
    def find_smallest_index(self, nums, pivot):
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                return i
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1, pin point out the index where the reverse sortdness ends from the back
        pivot = self.find_pivot(nums)
        if pivot == -1:
            self.reverse(nums, 0, len(nums) - 1)
        else:
            # I have to reverse the array and return it
        
            #  2, find out the smallest number that is greater than the numbet at pin index
            smallest_index = self.find_smallest_index(nums, pivot)
            nums[pivot], nums[smallest_index] = nums[smallest_index], nums[pivot]

            # 3, reverse it to make it sorted
            self.reverse(nums, pivot + 1, len(nums) - 1)


        