class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []

        universal = [0 for i in range(26)]
        for word in words2:
            letter = [0 for i in range(26)]
            for char in word:
                letter[ord(char) - ord('a')] += 1
            
            for i in range(26):
                universal[i] = max(universal[i], letter[i])
        
        for word in words1:
            letter = [0 for i in range(26)]
            for char in word:
                letter[ord(char) - ord('a')] += 1
            
            for i in range(26):
                if universal[i] > letter[i]:
                    break
            else:
                res.append(word)
        return res