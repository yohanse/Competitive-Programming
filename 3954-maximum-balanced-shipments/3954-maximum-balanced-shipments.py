class Solution:
    def maxBalancedShipments(self, weights: List[int]) -> int:
        max_weight = -float("inf")
        number_of_balanced_subarray = 0

        for weight in weights:
            max_weight = max(weight, max_weight)
            if weight < max_weight:
                number_of_balanced_subarray += 1
                max_weight = -float("inf")
        
        return number_of_balanced_subarray     