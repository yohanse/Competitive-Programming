class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def check(nums):
            sumi = 0
            flag = False
            for i in nums:
                sumi += max(i, 1)
                flag = flag or (i == 0)
            return sumi, flag
        
        sumi1, flag1 = check(nums1)
        sumi2, flag2 = check(nums2)

        if sumi1 == sumi2:
            return sumi1
        elif flag1 == flag2 == False:
            return -1
        elif sumi1 > sumi2 and flag2 == False:
            return -1
        elif sumi2 > sumi1 and flag1 == False:
            return -1
        else:
            return max(sumi1, sumi2)
        