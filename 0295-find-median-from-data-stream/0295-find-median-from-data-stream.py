'''
first_heap = [1] ---> max_heap

second_heap = [2] ----> min_heap

2, 1, 3, 4, 5, 6

if 

1, 2, 3

first = [-1, -2]
second = [3]

'''


class MedianFinder:

    def __init__(self):
        self.first_heap = []
        self.second_heap = []
        self.is_odd = False

    def addNum(self, num: int) -> None:
        self.is_odd = not self.is_odd

        heappush(self.first_heap, -num)
 
        if (self.second_heap == [] and len(self.first_heap) > 1) or len(self.first_heap) > len(self.second_heap) + 1:
            heappush(self.second_heap, -heappop(self.first_heap))
        elif self.second_heap != [] and self.second_heap[0] < -self.first_heap[0]:
            x, y = -heappop(self.first_heap), heappop(self.second_heap)
            heappush(self.second_heap, x)
            heappush(self.first_heap, -y)


    def findMedian(self) -> float:
        if self.is_odd:
            return -self.first_heap[0]
        
        return (-self.first_heap[0] + self.second_heap[0]) / 2
    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()