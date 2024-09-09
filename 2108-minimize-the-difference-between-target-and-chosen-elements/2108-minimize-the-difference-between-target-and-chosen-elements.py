class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        add = set([0])
        for r in range(len(mat)):
            temp = set()
            for c in range(len(mat[0])):
                for k in add:
                    temp.add(k + mat[r][c])
            add = temp
            
        result = inf
        for k in add:
            result = min(result, abs(k - target))
        return result