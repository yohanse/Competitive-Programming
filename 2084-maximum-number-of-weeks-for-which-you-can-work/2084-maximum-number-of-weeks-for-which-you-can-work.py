class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if sum(milestones) < 2*max(milestones):
            return 2*(sum(milestones) - max(milestones)) + 1
        return sum(milestones)
        