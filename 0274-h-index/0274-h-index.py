class Solution:
    def checker(self, possible_h, citations):
        count = 0
        for citation in citations:
            if citation >= possible_h:
                count += 1
        return count >= possible_h

    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, max(citations)
        while l < r:
            possible_h = (l + r + 1) // 2
            if self.checker(possible_h, citations):
                l = possible_h
            else:
                r = possible_h - 1
        return l
            
        