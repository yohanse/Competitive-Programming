class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def good_function(mid):
            return mid // a + mid // b + mid // c - mid // (math.lcm(a, b)) - mid // (math.lcm(a, c)) - mid // (math.lcm(c, b)) + mid // (math.lcm(a, b, c)) >= n


        l, r = 0, n * min(a, b, c)
        while l < r:
            mid = (l + r) // 2
            if good_function(mid):
                r = mid
            else:
                l = mid + 1
        return l