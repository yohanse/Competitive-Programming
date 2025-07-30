class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums):
            if len(nums) < 2:
                return nums, 0
            
            mid = len(nums) // 2
            left, l_ans = merge_sort(nums[:mid])
            right, r_ans = merge_sort(nums[mid:])
            return combine(left, right, l_ans, r_ans)
        
        def combine(left, right, l_ans, r_ans):
            merged = []
            p1 = p2 = 0
            count = 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] > right[p2]*2:
                    p2 += 1
                    count += len(left) - p1
                else:
                    p1 += 1
            
            p1 = p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] > right[p2]:
                    merged.append(right[p2])
                    p2 += 1
                    
                else:
                    merged.append(left[p1])
                    p1 += 1
            
            while p1 < len(left):
                merged.append(left[p1])
                p1 += 1
            
            while p2 < len(right):
                merged.append(right[p2])
                p2 += 1
            
            return merged, l_ans + r_ans + count
        
        return merge_sort(nums)[1]
            
            