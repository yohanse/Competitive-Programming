class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        maxi = min(nums)
        answer = inf
        nums = [-num for num in nums]     
        heapify(nums)
        
        while (-nums[0]) % 2 == 0:
            remove = -heappop(nums)
            answer = min(answer, remove - maxi)
            heappush(nums, -remove // 2)
            maxi = min(maxi, remove // 2)
        return min(answer, -heappop(nums) - maxi)

        