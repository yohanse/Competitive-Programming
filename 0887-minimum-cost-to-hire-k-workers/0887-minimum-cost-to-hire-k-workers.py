class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        index = [i for i in range(n)]
        index.sort(key=lambda x: wage[x] / quality[x])

        sumi = 0
        heap = []
        answer = inf
        for i in range(n):
            sumi += quality[index[i]]
            heappush(heap, -quality[index[i]])
            if i >= k - 1:
                answer = min(answer, sumi * (wage[index[i]] / quality[index[i]]))
                sumi += heappop(heap)
        return answer