class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        previous_count = {}

        for word in strs:
            letters = [0 for _ in range(26)]
            for char in word:
                letters[ord(char) - ord("a")] += 1
            
            tuple_letters = tuple(letters)
            if tuple_letters not in previous_count:
                previous_count[tuple_letters] = []
            
            previous_count[tuple_letters].append(word)
        
        
        return list(previous_count.values())