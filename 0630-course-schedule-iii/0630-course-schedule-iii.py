class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x : x[1])
        num = []
        time = 0
        for duration, lastday in courses:
            if time + duration <= lastday:
                heappush(num, -duration)
                time += duration
            else:
                if num:
                    x = -heappop(num)
                    if x > duration and time - x + duration <= lastday:
                        heappush(num, -duration)
                        time = time - x + duration
                    else:
                        heappush(num, -x)
        return len(num) 
