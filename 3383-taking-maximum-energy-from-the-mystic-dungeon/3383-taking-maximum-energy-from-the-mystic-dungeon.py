class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        leng = len(energy)
        dp = [0 for i in range(leng + k)]
        for i in range(leng):
            dp[i + k] = max(dp[i], 0) + energy[i]
        return max(dp[leng:])