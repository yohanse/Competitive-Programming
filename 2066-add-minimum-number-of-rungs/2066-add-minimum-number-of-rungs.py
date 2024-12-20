class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = count = 0
        for i in range(len(rungs)):
            count += (rungs[i] - prev - 1) // dist
            prev = rungs[i]
        return count