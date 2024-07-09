class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        heap = [0]
        n = len(s)

        for i in range(1, n):
            while heap and i > heap[0] + maxJump:
                heappop(heap)

            if s[i] == "0" and heap and heap[0] + minJump <= i <= heap[0] + maxJump:
                heappush(heap, i)
        return (n - 1 ) in heap