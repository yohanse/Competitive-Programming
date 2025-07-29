class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = s.count("0")
        so_far_zero = so_far_one = 0

        result = min(len(s), zeros)
        for i in range(len(s)):
            if s[i] == "1":
                so_far_one += 1
            else:
                so_far_zero += 1
            
            result = min(result, so_far_one + zeros - so_far_zero)
        
        return result