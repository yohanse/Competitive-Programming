class Solution:
    def is_valid(self, t, prices, k):
        count = 0
        prev = -inf

        for i in range(len(prices)):
            if prices[i] - prev >= t:
                count += 1
                prev = prices[i]
        
        return count >= k
            
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l, r = 0, max(price) - min(price)
        while r > l:
            mid = (l + r + 1) // 2
            if self.is_valid(mid, price, k):
                l = mid
            else:
                r = mid - 1
        return l