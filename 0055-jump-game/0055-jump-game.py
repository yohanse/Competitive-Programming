class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_go, current = nums[0], 0
        next = can_go
        while current <= min(can_go, len(nums) - 1):
            next = max(next, current + nums[current])
            current += 1
            if current >= can_go:
                can_go = next

        return can_go >= len(nums) - 1

