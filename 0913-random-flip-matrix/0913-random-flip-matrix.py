class Solution:

    def __init__(self, m: int, n: int):
        self.void = set()
        self.size = n*m - 1
        self.rows = n

    def flip(self) -> List[int]:
        num = randint(0, self.size)
        while num in self.void:
            num = randint(0, self.size)
        self.void.add(num)
        return [num//self.rows, num%self.rows]

    def reset(self) -> None:
        self.void = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()