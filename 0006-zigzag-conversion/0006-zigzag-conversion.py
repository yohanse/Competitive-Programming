class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cols = len(s) // (numRows - 1) + 1
        zigzag = [["" for _ in range(cols)] for _ in range(numRows)]

        index = 0
        col = 0
        while index < len(s):
            for i in range(numRows):
                if index < len(s):
                    zigzag[i][col] = s[index]
                    index += 1
            col += 1
            for i in range(numRows - 2, 0, -1):
                if index < len(s):
                    zigzag[i][col] = s[index]
                    index += 1
            col += 1
        
        result = []
        for i in range(numRows):
            for j in range(cols):
                if zigzag[i][j] != "":
                    result.append(zigzag[i][j])
        
        return "".join(result)
        