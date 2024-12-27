class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = count = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
                newInterval = [newInterval[0], max(intervals[i][1], newInterval[1])]
                
            elif intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[0]:
                newInterval = [intervals[i][0], max(intervals[i][1], newInterval[1])]
            else:
                intervals[l], intervals[i] = intervals[i], intervals[l]
                l += 1

        intervals.append(0)
        intervals[l] = newInterval

        return sorted(intervals[:l+1])

        
