class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True
        
        if "1" not in s or "1" not in target:
            return False
        
        return True