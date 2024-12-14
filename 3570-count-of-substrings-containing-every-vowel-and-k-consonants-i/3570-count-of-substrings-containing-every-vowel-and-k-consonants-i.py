class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        ans = 0
        for i in range(len(word)):
            vowels = {"a": 0, "e":0, "i":0, "o":0, "u":0}
            vowel_needed = 5
            consonant_have = 0
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    consonant_have += 1
                elif not vowels[word[j]]:
                    vowels[word[j]] = 1
                    vowel_needed -= 1

                if vowel_needed == 0 and consonant_have == k:
                    ans += 1
        return ans