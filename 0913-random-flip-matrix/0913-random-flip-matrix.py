class Solution:

    def __init__(self, m: int, n: int):
        self.void = set()
        self.m = m
        self.n = n

    def flip(self) -> List[int]:
        r, c = randint(0, self.m - 1), randint(0, self.n - 1)
        while (r, c) in self.void:
            r, c = randint(0, self.m - 1), randint(0, self.n - 1)
        self.void.add((r, c))
        return [r, c]
    def reset(self) -> None:
        self.void = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()