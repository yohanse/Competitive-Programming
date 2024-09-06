class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        binary = list(binary)
        l = -1
        for r in range(len(binary)):
            if binary[r] == "0":
                if l == -1:
                    l = r
                else:
                    l += 1

        res = ["1" for i in range(len(binary))]
        if l != -1:
            res[l] = "0"
            
        return "".join(res)

        