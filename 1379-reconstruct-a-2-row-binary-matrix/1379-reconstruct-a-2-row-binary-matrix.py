class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        two = colsum.count(2)
        upper, lower = upper - two, lower - two

        matrix = [[0 for i in range(len(colsum))] for j in range(2)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                matrix[0][i] = matrix[1][i] = 1
            
            if colsum[i] == 1:
                if upper != 0:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    lower -= 1
                    matrix[1][i] = 1
        
        if upper == lower == 0:
            return matrix
        return []

        