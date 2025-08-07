class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = -1
        two = len(nums) - 1

        while zero <= two:
            if nums[zero] == 1 and one == -1:
                    one = zero
            
            if nums[zero] == 0 and one != -1:
                    nums[zero], nums[one] = nums[one], nums[zero]
                    one += 1
            
            if nums[zero] == 2:
                while zero < two and nums[two] == 2:
                    two -= 1
                
                if zero < two:
                    nums[zero], nums[two] = nums[two], nums[zero]
                    two -= 1
                    zero -= 1
            
            zero += 1

        