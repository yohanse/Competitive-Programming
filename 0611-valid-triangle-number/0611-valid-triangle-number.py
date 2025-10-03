class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        valid_triangles = 0
        for c in range(2, len(nums)):
            a, b = 0, c - 1

            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    valid_triangles += b - a
                    b -= 1
                else:
                    a += 1
        return valid_triangles
                
        