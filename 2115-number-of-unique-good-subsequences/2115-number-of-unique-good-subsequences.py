class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        modulo = 10**9 + 7
        prev_ones = prev_zeros = curr = 0
        

        for i in binary:
            if i == "0" and curr == 0:
                continue
            
            if i == "0":
                temp = prev_zeros
                prev_zeros = curr
                curr = 2*curr - temp
                
            else:
                temp = prev_ones
                prev_ones = curr
                if curr == 0:
                    curr = 1
                else:
                    curr = 2*curr - temp
        one = 1 if "0" in binary else 0
        return (curr + one) % modulo
                