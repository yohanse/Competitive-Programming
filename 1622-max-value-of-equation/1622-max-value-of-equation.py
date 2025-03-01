class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue, result = deque(), -inf
        
        for x, y in points:
            while queue and x - queue[0][0] > k:
                queue.popleft()

            if queue:
                result = max(result, queue[0][1] - queue[0][0] + x + y)

            while queue and queue[-1][1] - queue[-1][0] < y - x:
                queue.pop()
            
            queue.append([x, y])
        return result