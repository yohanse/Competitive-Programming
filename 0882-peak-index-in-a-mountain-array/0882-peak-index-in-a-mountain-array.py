class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2
        while l < r:
            mid = (l + r) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
        