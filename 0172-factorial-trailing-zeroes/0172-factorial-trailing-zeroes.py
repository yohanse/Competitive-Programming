class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        two = five = 0
        for i in range(1, n + 1):
            num = i
            while num % 2 == 0:
                two += 1
                num //= 2
            
            num = i
            while num % 5 == 0:
                five += 1
                num //= 5
        return min(two, five)