class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        leng = len(nums1) // 2
        set_nums1 = set(nums1) 
        set_nums2 = set(nums2)

        alli = set(nums1 + nums2)
        count = []
        for i in alli:
            if i in set_nums1 and i in set_nums2:
                count.append((i, 2))
            elif i in set_nums1:
                count.append((i, 1))
            else:
                count.append((i, 0))
        count.sort(key=lambda x: x[1])
        nums1 = nums2 = ans = 0
        for a, b in count:
            if b == 1 and nums1 < leng:
                ans += 1
                nums1 += 1
            elif b == 0 and nums2 < leng:
                ans += 1
                nums2 += 1
            elif b == 2 and min(nums1, nums2) < leng:
                if nums1 < leng:
                    ans += 1
                    nums1 += 1
                else:
                    ans += 1
                    nums2 += 1
        
        return ans
