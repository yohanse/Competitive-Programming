class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = [0, 0, 0]
        one = [0, 0, 0]

        for i in s:
            if i == "1":
                one = [one[0] + 1, one[1] + zero[0], one[2] + zero[1]]
            else:
                zero = [zero[0] + 1, zero[1] + one[0], zero[2] + one[1]]
        return one[2] + zero[2]