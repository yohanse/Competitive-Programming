class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        chossen_triplets = set()
        nums.append(-inf)
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                l, r = i + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] == 0:
                        chossen_triplets.add((nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] + nums[i] > 0:
                        r -= 1
                    else:
                        l += 1
        return [[a, b, c] for a, b, c in chossen_triplets]
                    
