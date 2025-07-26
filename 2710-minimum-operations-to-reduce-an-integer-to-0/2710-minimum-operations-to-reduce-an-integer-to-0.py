class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n > 0:
            if (n & (n >> 1)) == 0:
                # no adjacent 1s, just count the number of 1s
                return count + bin(n).count('1')
            # find the lowest bit where two 1s are adjacent
            lowest_adjacent = 1
            while (n & (lowest_adjacent << 1)) == 0 or (n & lowest_adjacent) == 0:
                lowest_adjacent <<= 1
            # add to that position to carry and clear adjacent 1s
            n += lowest_adjacent
            count += 1
        return count

            