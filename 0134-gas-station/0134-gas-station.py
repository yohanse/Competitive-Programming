class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas += gas
        cost += cost

        n = len(gas)
        prefix_sum = 0
        l = 0
        for i in range(n):
            
            prefix_sum +=  (gas[i] - cost[i])

            if prefix_sum < 0:
                prefix_sum = 0
                l = i + 1
            
            if l == i + 1 - (n//2):
                return l
            
            
            
        return -1
        