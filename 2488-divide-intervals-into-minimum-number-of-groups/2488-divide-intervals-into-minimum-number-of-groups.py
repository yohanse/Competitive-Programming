class Solution:
    def minGroups(self, array: List[List[int]]) -> int:
        array.sort(key=lambda x:(x[0],x[1]))
        minHeap=[]
        counter=0
        heapq.heappush(minHeap,array[0][1])
        counter+=1
        for lefti, righti in array[1:]:
            if lefti > minHeap[0]:
                heapq.heappop(minHeap)
            else:
                counter+=1
            heapq.heappush(minHeap,righti)
        return counter