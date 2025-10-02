class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = len(queries)
        result = [0 for _ in range(m)]
        for i in range(m):
            a, b = queries[i]
            num_edges = 1
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                num_edges += 1
            result[i] = num_edges
        return result
        