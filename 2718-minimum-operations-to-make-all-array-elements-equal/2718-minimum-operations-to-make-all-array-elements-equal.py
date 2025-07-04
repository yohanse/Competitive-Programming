class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        index = [i for i in range(len(queries))]
        answer = [0 for i in range(len(queries))]
        index.sort(key=lambda x:queries[x])


        prefix_sum = 0
        postfix_sum = sum(nums)
        pointer = 0
        for i in range(len(queries)):
            while pointer < len(nums) and nums[pointer] < queries[index[i]]:
                prefix_sum += nums[pointer]
                postfix_sum -= nums[pointer]
                pointer += 1
            answer[index[i]] = pointer*queries[index[i]] - prefix_sum + postfix_sum - (len(nums) - pointer)*queries[index[i]]
        return answer


        