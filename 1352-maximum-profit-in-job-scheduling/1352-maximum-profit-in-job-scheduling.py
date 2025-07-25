class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        import bisect

        # Step 1: Combine and sort jobs by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Step 2: dp will store (endTime, maxProfit)
        dp = [(0, 0)]  # base case: before any job
        
        for s, e, p in jobs:
            # Binary search to find the latest job that ends before s
            i = bisect.bisect_right(dp, (s, float('inf'))) - 1
            current_profit = dp[i][1] + p

            # Only add this if it's better than the last max profit
            if current_profit > dp[-1][1]:
                dp.append((e, current_profit))

        return dp[-1][1]
