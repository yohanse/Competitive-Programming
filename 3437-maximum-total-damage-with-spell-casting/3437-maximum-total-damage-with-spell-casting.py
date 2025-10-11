class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = list(Counter(power).items())
        counter.sort()
        
        queue = deque()
        for i in range(len(counter)):
            
            
            while len(queue) > 1 and queue[1][0] < counter[i][0] - 2:
                damage, tot_damage = queue.popleft()
                queue[0][1] = max(queue[0][1], tot_damage)
            
            prev_damage = 0
            if queue and queue[0][0] < counter[i][0] - 2:
                _, prev_damage = queue[0]
            
            queue.append([counter[i][0], prev_damage + counter[i][0]*counter[i][1]])
        
        return max([damage for _, damage in queue])