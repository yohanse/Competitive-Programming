class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def func(string):
            i = j = 0
            while i < N and j < len(string):
                if string[j] == pattern[i]:
                    i += 1
                elif string[j].isupper():
                        return False
                j += 1

            while j < len(string):
                if string[j].isupper():
                    return False
                j += 1
                
            return i == N

        N = len(pattern)
        for index, string in enumerate(queries):
            queries[index] = func(string)     
        return queries    