class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        


        def good_function(mid, nums):
            length_nums = len(nums)
            frequency_reminder = {}
            for i in range(length_nums):
                reminder = nums[i] % value
                frequency_reminder[reminder] = frequency_reminder.get(reminder, 0) + 1

            for i in range(mid):
                reminder = i % value
                if not frequency_reminder.get(reminder, 0):
                    return False
                frequency_reminder[reminder] -= 1
            return True


        l, r = 0, len(nums)
        while l < r:
            mid = (l + r + 1) // 2
            if good_function(mid, nums.copy()):
                l = mid
            else:
                r = mid - 1
        return l
        