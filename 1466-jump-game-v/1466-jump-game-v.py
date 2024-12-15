class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)

        dp = [0 for i in range(N)]
        index = [i for i in range(N)]
        index.sort(key = lambda x: arr[x])

        for i in range(N):
            key = arr[index[i]]

            for j in range(1, d + 1):
                if index[i] + j < N and arr[index[i]] > arr[index[i] + j]:
                    dp[index[i]] = max(dp[index[i]], dp[index[i] + j] + 1)
                else:
                    break

            for j in range(1, d + 1):
                if index[i] - j > -1 and arr[index[i]] > arr[index[i] - j]:
                    dp[index[i]] = max(dp[index[i]], dp[index[i] - j] + 1)
                else:
                    break

        return max(dp) + 1
        