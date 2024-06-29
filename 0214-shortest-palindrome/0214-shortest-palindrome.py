class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = 2*len(s) + 1
        dp = [0 for i in range(length)]
        array = ["#" for i in range(length)]

        for i in range(1, length, 2):
            array[i] = s[i//2]
        
        
        left = right = 0
        answer = 0

        for index in range(length):
            dp[index] = max(0, min(dp[left + right - index], right - index))
            while index - dp[index] > -1 and index + dp[index] < length and array[index - dp[index]] == array[index + dp[index]]:
                dp[index] += 1

            if index + dp[index] > right:
                left, right = index - dp[index], index + dp[index]

        
            if index - dp[index] in [-1, 0]:
                palindrome_length = (2*(dp[index] - 1) + 1) // 2
                answer = max(answer, palindrome_length)

        return s[answer:][::-1] + s

            

        