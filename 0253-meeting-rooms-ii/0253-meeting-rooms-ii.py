class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        max_overlap = 0
        for start, end in intervals:
            while heap and start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
            max_overlap = max(max_overlap, len(heap))
        return max_overlap
        