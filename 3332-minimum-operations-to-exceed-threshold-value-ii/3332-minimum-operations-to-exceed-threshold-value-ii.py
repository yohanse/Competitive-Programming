class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0

        heapify(nums)
        while len(nums) > 1:
            x, y = heappop(nums), heappop(nums)
            if x >= k:
                return count  
            heappush(nums, 2*x + y)
            count += 1
        return count      