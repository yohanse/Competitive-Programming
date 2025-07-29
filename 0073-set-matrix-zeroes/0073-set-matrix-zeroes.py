class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for x in range(len(matrix)):
                        if matrix[x][j] != 0:
                            matrix[x][j] = "#"

                    for x in range(len(matrix[0])):
                        if matrix[i][x] != 0:
                            matrix[i][x] = "#"
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
