class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, num):
        curr_root = self.root
        for i in range(29, -1, -1):
            curr = 2**i

            if curr & num:
                if not curr_root.one:
                    curr_root.one = TrieNode()
                curr_root = curr_root.one
            else:
                if not curr_root.zero:
                    curr_root.zero = TrieNode()
                curr_root = curr_root.zero

    def find(self, num):
        curr_root = self.root
        if curr_root.one == curr_root.zero == None:
            return -1
        ans = 0
        for i in range(29, -1, -1):
            curr = 2**i
            if curr & num:
                if not curr_root.zero:
                    
                    curr_root = curr_root.one
                else:
                    ans += curr
                    curr_root = curr_root.zero
            else:
                if not curr_root.one:
                    
                    curr_root = curr_root.zero
                else:
                    ans += curr
                    curr_root = curr_root.one
        return ans





class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        
        index = [i for i in range(len(queries))]
        index.sort(key=lambda x:queries[x][1])
        trie = Trie()
        answer = [0 for i in range(len(queries))]
        l = 0
        for i in range(len(queries)):
            while l < len(nums) and queries[index[i]][1] >= nums[l]:
                trie.add(nums[l])
                l += 1

            answer[index[i]] = trie.find(queries[index[i]][0])
        return answer