class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        n = len(s)

        for i in range(1, n):
            while queue and i > queue[0] + maxJump:
                queue.popleft()

            if s[i] == "0" and queue and queue[0] + minJump <= i <= queue[0] + maxJump:
                queue.append(i)
        return (n - 1 ) in queue