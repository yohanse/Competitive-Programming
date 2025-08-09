class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [0 for _ in range(len(w))]
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]
        self.sum = self.prefix_sum[-1]
        self.length = len(w)

    def pickIndex(self) -> int:
        target = self.sum*random.random()
        l, r = 0, self.length - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()