class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        operations = 0
        while n:
            largest_factor = 1
            square_root = int(n**0.5)
            for factor in range(2, square_root + 1):
                if n % factor == 0:
                    largest_factor = n // factor
                    break
            else:
                return n + operations
            
            operations += n // largest_factor
            n = largest_factor
        
