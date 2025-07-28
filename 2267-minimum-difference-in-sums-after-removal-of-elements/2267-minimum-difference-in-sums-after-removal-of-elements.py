class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        
        mini_left = [0 for i in range(n + 1)]
        heap = []
        for i in range(n):
            heappush(heap, -nums[i])
        mini_left[0] = sumi = -sum(heap)
        for i in range(n, 2*n):
            if -heap[0] > nums[i]:
                sumi = sumi + heap[0] + nums[i]
                heappop(heap)
                heappush(heap, -nums[i])
            mini_left[i - n + 1] = sumi

        
        max_right = [0 for i in range(n + 1)]
        heap = []
        for i in range(3*n - 1, 2*n - 1, -1):
            heappush(heap, nums[i])
        max_right[-1] = sumi = sum(heap)
        for i in range(2*n - 1, n - 1, -1):
            if heap[0] < nums[i]:
                sumi = sumi - heap[0] + nums[i]
                heappop(heap)
                heappush(heap, nums[i])
            max_right[i - n] = sumi


        max_difference = inf
        for i in range(n + 1):
            diff = mini_left[i] - max_right[i]
            max_difference = min(max_difference, diff)
        return max_difference