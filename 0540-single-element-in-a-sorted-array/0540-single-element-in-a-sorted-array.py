class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if r == 0:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if r - l == 2:
                if nums[l] != nums[l + 1]:
                    return nums[l]
                return nums[r] 

            elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid] != nums[mid - 1]:
                if (mid - l) % 2:
                     
                    r = mid - 1
                else:
                    l = mid
            else:
                if (mid - l) % 2 == 0:
                     
                    r = mid
                else:
                    l = mid + 1
