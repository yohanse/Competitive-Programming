class Solution:
    def good_function(self, price, testiness, bucket_size):
        prev = price[0]
        curr_bucket_size = 1
        for i in range(len(price)):
            if price[i] - prev >= testiness:
                prev = price[i]
                curr_bucket_size += 1
        return curr_bucket_size >= bucket_size

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l, r = 0, max(price) - min(price)
        while l < r:
            mid = (l + r + 1) // 2
            if self.good_function(price, mid, k):
                l = mid
            else:
                r = mid - 1
        return l