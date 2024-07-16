class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = [0 for i in range(26)]
        for i in range(len(s)):
            last_occurence[ord(s[i]) - ord("a")] = i
        
        up_to = last = 0
        result = []
        for i in range(len(s)):
            if i > up_to:
                result.append(i - last)
                last = i
            up_to = max(up_to, last_occurence[ord(s[i]) - ord("a")])

        if len(s) - last != 0:
            result.append(len(s) - last)

        return result


