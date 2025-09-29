class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        previous_prefix_sum = defaultdict(int)
        previous_prefix_sum[0] += 1

        count_sub_array = 0
        for r in range(len(nums)):
            prefix_sum += nums[r]
            count_sub_array += previous_prefix_sum[prefix_sum - k]
            previous_prefix_sum[prefix_sum] += 1
        
        return count_sub_array


        