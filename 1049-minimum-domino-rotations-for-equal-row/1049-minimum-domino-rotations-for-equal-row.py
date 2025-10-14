class Solution:
    def count_rotate(self, tops, bottoms, target):
        rotate_count = 0
        for i in range(len(tops)):
            if tops[i] == target:
                continue
            
            if bottoms[i] == target:
                rotate_count += 1
            else:
                return float("inf")
        
        return rotate_count

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_rotate_count = float("inf")

        for target in range(1, 7):
            min_rotate_count = min(min_rotate_count, self.count_rotate(tops, bottoms, target), self.count_rotate(bottoms, tops, target))
        
        if min_rotate_count == float("inf"):
            return -1
        return min_rotate_count