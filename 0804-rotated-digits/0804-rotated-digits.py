class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0

        for num in range(1, n + 1):
            is_different = False
            is_valid = True

            while num:
                digit = num%10

                if digit in [3, 4, 7]:
                    is_valid = False
                
                if digit in [2, 5, 6, 9]:
                    is_different = True
                
                num //= 10
            
            if is_valid and is_different:
                count += 1
        return count