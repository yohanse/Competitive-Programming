class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # lets start with the brute we can choose a target that might be min(nums) to max(nums) we will iterate throught each target and we will calculate the cost it woudld take as to change each number to target so the time complexity will be (max(nums) - min(nums))*len(nums) and sapce of O(1) so the time is like m*n n is the length of the nums and m- the rang of nums

        # so either we should optimize the caculation of the cost or the search of the target because on the above appraoch they take us linear time 

        # lets check if we can optimize the caulation of a cost I do not think it is possible because can't calulate as a group so what I am advising over hear is optimizing the search of a target

        # lets assume that we have best target called x and as we choose a traget the is less than x and greater than x the cost will be increase so when you draw a grph cost versus target it will give us reversed mountian so that is the technique

        # based on the above fact, we can do better search using binary search we dont stop until we got a point where the cost is better than it is negihbors(means x + 1, and x - 1)

        # so based on the above appraoch we reduce the time complexity to the nlogn

        # lets see some edge case the graph might not be a direct reverse mountian sometime it might be increasing leaner which leads as the naaswer on the first or decreasing linear which is the answer the last one (the maximum one)

        # so inorder to mitigate the above edge case we can add 1 and subtract one to the search whihc meand target is in between min(nums) - 1 to max(nums) + 1
        # we can prove this one using the same assumtion on we have used

        # lets right the code


        def calculate_cost(nums, costs, target):
            tot_cost = 0
            for i in range(len(nums)):
                tot_cost += abs(target - nums[i])*costs[i]
            return tot_cost

        l, r = min(nums) - 1, max(nums) + 1
        while l < r:
            mid = (l + r) // 2
            past, present, future = calculate_cost(nums, cost, mid - 1), calculate_cost(nums, cost, mid), calculate_cost(nums, cost, mid + 1)
            if past >= present <= future:
                return present
            elif past <= present:
                r = mid
            else:
                l = mid + 1
        
            
        