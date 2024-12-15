class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit)
        arr = [[startTime[i], endTime[i], profit[i]] for i in range(N)]
        arr.sort(key=lambda x: x[1])

        # stack = list of ( end, max_price_up_to_this)
        stack = [[0, 0]]

        def binary_search(target):
            left, right = 0, len(stack) - 1
            
            while left < right:
                mid = (left + right + 1) // 2
                if stack[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid
            return left
        ans = 0
        for start, end, profit in arr:
            index = binary_search(start)
            stack.append([end, max(profit + stack[index][1], stack[-1][1])])
            ans = max(ans, stack[-1][1])
        print(arr)
        print(stack)
        return ans
        