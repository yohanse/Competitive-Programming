class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        dictionary = {}
        for i in nums:
            reminder = i%space
            dictionary[reminder] = dictionary.get(reminder, 0) + 1
            
        maxi = max(dictionary.values())
        for i in nums:
            reminder = i%space
            if dictionary[reminder] == maxi:
                return i
        
        
        