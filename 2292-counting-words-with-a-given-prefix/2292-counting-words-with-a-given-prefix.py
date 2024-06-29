class TrieNode:
    def __init__(self):
        self.frq = 0
        self.children = [None for i in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        curr = self.root
        for i in range(len(string)):
            if not curr.children[ord(string[i]) - ord("a")]:
                curr.children[ord(string[i]) - ord("a")] = TrieNode()
                
            curr = curr.children[ord(string[i]) - ord("a")]
            curr.frq += 1
    
    def search(self, string):
        curr = self.root
        for i in range(len(string)):
            if not curr.children[ord(string[i]) - ord("a")]:
                return 0
            curr = curr.children[ord(string[i]) - ord("a")]
        return curr.frq


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.search(pref)
        