class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        hamm_dis = 0
        for i in range(32):
            zero = one = 0
            for num in nums:
                number = 2**i
                if number & num:
                    one += 1
                else:
                    zero += 1
            hamm_dis += (zero*one)
        return hamm_dis