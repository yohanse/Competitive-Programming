class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp = {}
        if ((maxChoosableInteger * (maxChoosableInteger + 1))//2) < desiredTotal:
            return False
            
        @cache
        def recursive(seen, prev, turn, score):
            if score >= desiredTotal:
                return prev
                
            

            num = not turn
            for i in range(maxChoosableInteger):
                if not ((seen >> i) & 1):
                    seen = seen | (1 << i)
                    

                    if turn:
                        num = num or recursive(seen, turn, not turn, score + 1 + i)
                    else:
                        num = num and recursive(seen, turn, not turn, score + 1 + i)

                    seen = seen & (~(1 << i))
                    
            return num

        return recursive(0, True, True, 0)