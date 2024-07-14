class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic, answer = {}, -inf
        count = prefix_sum = 0
        
        for num in nums:
            dic[num] = min(dic.get(num, inf), prefix_sum)
            prefix_sum += num
            answer = max(answer, prefix_sum - min(dic.get(num - k, inf), dic.get(k + num, inf)))
          
        return answer if answer != -inf else 0   