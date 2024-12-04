class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        leng = len(nums)
        max_queue = deque()
        min_queue = deque()

        l = ans = 0
        for r in range(leng):
            while max_queue and nums[max_queue[-1]] > nums[r]:
                max_queue.pop()
            
            while min_queue and nums[min_queue[-1]] < nums[r]:
                min_queue.pop()
            
            max_queue.append(r)
            min_queue.append(r)
            
            while nums[min_queue[0]] - nums[max_queue[0]] > 2:
                if max_queue[0] == l:
                    max_queue.popleft()

                if min_queue[0] == l:
                    min_queue.popleft()
                ans += r - l
                l += 1
        arch = leng - l

        return ans  + (arch*(arch + 1) // 2)