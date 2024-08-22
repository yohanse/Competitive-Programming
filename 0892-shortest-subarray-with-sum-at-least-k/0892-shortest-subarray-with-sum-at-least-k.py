class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        q = deque([(0, -1)])
        tot = 0


        ans = sys.maxsize
        for i, num in enumerate(nums):
            tot += num
            while q and q[-1][0] >= tot:
                q.pop()
            

            while q and tot - q[0][0] >= k:
                ans = min(ans, i - q[0][1])
                q.popleft()
            
            q.append((tot,i))
             
        return -1 if ans==sys.maxsize else ans
        