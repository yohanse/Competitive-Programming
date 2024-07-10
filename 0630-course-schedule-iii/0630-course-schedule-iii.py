class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x : x[1])
        heap, time = [], 0
        for duration, lastday in courses:
            if time + duration <= lastday:
                heappush(heap, -duration)
                time += duration
           
            elif heap and heap[0] + duration < 0 and time + heap[0] + duration <= lastday:
                time = time + heap[0] + duration
                heappop(heap)
                heappush(heap, -duration)
                
        return len(heap) 