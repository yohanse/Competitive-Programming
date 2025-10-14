class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        remainder_map = {}
        count = 0
        for num in arr:
            remainder = num%k
            if remainder == 0 and remainder_map.get(0, 0) != 0:
                remainder_map[0] -= 1
                count += 1
            elif remainder_map.get(k - remainder, 0) != 0:
                remainder_map[k - remainder] -= 1
                count += 1
            else:
                remainder_map[remainder] = remainder_map.get(remainder, 0) + 1
        return count == len(arr) // 2
        

            