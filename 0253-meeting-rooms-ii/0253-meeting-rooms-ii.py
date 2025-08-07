class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        max_conference_room = 1
        heap = []
        rooms = 0
        for start, end in intervals:
            while heap and heap[0] <= start:
                heappop(heap)
                rooms -= 1

            heappush(heap, end)
            rooms += 1
            max_conference_room = max(max_conference_room, rooms)
        return max_conference_room
