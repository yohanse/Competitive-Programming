class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water_amount = 0
        l, r = 0, len(height) - 1
        while r > l:
            water_amount = min(height[l], height[r])*(r - l)
            max_water_amount = max(max_water_amount, water_amount)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_water_amount