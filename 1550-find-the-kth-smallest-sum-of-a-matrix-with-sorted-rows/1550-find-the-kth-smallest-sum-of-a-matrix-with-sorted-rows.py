class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])
        index = [0 for i in range(n)]
        heap = [(sum([mat[i][0] for i in range(n)]), index)]
        visite = set([tuple(index)])
        
        while k - 1:
            sumi, index = heappop(heap)
            
            for i in range(n):
                index[i] += 1
                if index[i] < m and tuple(index) not in visite:
                    heappush(heap, (sum([mat[i][index[i]] for i in range(n)]), index.copy()))
                    visite.add(tuple(index))
                index[i] -= 1
            k -= 1
      
        return heap[0][0]

        