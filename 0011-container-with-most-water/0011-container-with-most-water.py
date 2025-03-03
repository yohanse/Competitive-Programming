class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        while r > l:
            water = max(water, (r-l) * (min(height[l],height[r])))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return water