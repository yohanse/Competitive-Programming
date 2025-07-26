class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def permutaion(perm, visited):
            if len(perm) == len(nums):
                permutations.append(perm.copy())
                return
            
            for num in nums:
                if num not in visited:
                    perm.append(num)
                    visited.add(num)
                    permutaion(perm, visited)
                    perm.pop()
                    visited.remove(num)
        permutaion([], set())
        return permutations