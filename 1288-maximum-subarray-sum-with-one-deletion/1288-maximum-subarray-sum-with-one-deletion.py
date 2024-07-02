class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        result = sum(arr)
        n = len(arr)
        left = [0 for _ in range(n + 1)]
        right = [0 for i in range(n + 1)]

        for i in range(n):
            left[i + 1] = max(left[i] + arr[i], 0)

        for i in range(n - 1, -1, -1):
            right[i] = max(right[i + 1] + arr[i], 0)
        
        for i in range(n):
            result = max(result, left[i] + right[i + 1])
        
        return max(arr) if result == 0 and result not in arr else result
        
        