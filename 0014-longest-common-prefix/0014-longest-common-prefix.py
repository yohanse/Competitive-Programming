class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rows = len(strs)
        cols = min([len(string) for string in strs])

        longest_common_prefix = []
        for col in range(cols):
            for row in range(1, rows):
                if strs[row - 1][col] != strs[row][col]:
                    return "".join(longest_common_prefix)
            longest_common_prefix.append(strs[0][col])
        
        return "".join(longest_common_prefix)

        