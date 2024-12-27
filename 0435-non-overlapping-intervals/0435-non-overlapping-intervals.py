class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        max_end = -inf
        count = 0
        for start, end in intervals:
            if start >= max_end:
                count += 1
                max_end = max(max_end, end)
        return len(intervals) - count