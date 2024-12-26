class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -inf
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            max_product = max(max_product, product)
            if product == 0:
                product = 1

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            max_product = max(max_product, product)
            if product == 0:
                product = 1
        return max_product
            