class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MODULO = 1337
        def rec(base, leading, zeros):
            if zeros == 0:
                return pow(a, leading, MODULO)
            return pow(rec(base, leading, zeros - 1), 10, MODULO)

        n, product = len(b), 1
        for i in range(n):
            if b[i]:
                product = (product * rec(a, b[i], n - i - 1)) % MODULO
        return product

        