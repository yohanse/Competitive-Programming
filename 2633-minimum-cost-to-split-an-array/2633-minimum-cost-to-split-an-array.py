class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # When we start with the brute force we can generate all possible split of subarray and find out the minimum sum of importance for this it might 2**n because for each number we can add to exisitng subarry or create new one that is why and the space complexity will o(n) because we have to collect the subarray because at the end we need to run trimmed so also we will ahve additional time complexity so ttal time = n*2**n

        # Certainly the brute will fall since n might up to 1000

        # lets go to the optimal one 

        # I am not sure where to begin so lets start with number of subarray lets see the effect 

        # assume the number of summary is m

        # the answer = m*k + sum(trimmed[subarray[i]]); i is 0 - m

        # I think there some kind of dynamic programming over here we can asumme that 

        # let me simulate with in example because it very easy with in example

        # the given array      1, 2, 1, 2, 1, 3, 3
        # the answer           3, 

        # the answer for a single element is k + num[0] = 2 + 1 = 3
        # for the second elemt we have two choice either we grouped with one as single subaary the cost will be k + sum(trimmed[1, 2]) = 2 + 1 + 2 = 5
        # the second choice is to make it a single subarray which lead us two arrays [1] and [2] here is the the dyanmic programming came to rescue us because we have know the best answer for [1] is 3 and we need to calculate for [2] will be 2 + 2 = 4 so the total will be 4 + 3 = 7

        # hence we have two choice we will choose the minimum one because we have asked for the minimum cost in our case will be min(7, 5) = 5 so the best answer till index 1 which means [1, 2] if they are standalone array the answer will be 5 and we will ccontinue till we got to the end

        # the time complexity will o(n**2) and the space is O(n)

        # I will wirte the code wuickly if you don't have any question

        n = len(nums)
        dp = [inf for i in range(n + 1)] # to add pagination
        dp[0] = 0

        for i in range(n):
            freq = {}
            value = 0
            for j in range(i, -1, -1):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
                if freq[nums[j]] == 1:
                    value += 1
                
                if freq[nums[j]] == 2:
                    value -= 1
                
                dp[i + 1] = min(dp[i + 1], dp[j] + i - j + 1 - value + k)
            
        return dp[-1]

        