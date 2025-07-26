class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        number_of_overlapp = 0
        end = -inf
        print(intervals)
        for a, b in intervals:
            if a < end:
                number_of_overlapp += 1
                end = min(end, b)
            else:
                end = b
        return number_of_overlapp