class Solution:
    def chr_ord(self, letter):
        return ord(letter) - ord('a')
    
    def ord_chr(self, num):
        return chr(num + ord('a'))

    def find_edge(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return [self.chr_ord(word1[i]), self.chr_ord(word2[i])]
        if len(word1) > len(word2):
            return False
        return [self.chr_ord(word1[0]), self.chr_ord(word2[0])]

    def alienOrder(self, words: List[str]) -> str:
        graph = [[] for _ in range(26)]
        indegree = [0 for i in range(26)]
        participants = set(list(words[0]))
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            
            
            for char in word2:
                participants.add(char)

            edge = self.find_edge(word1, word2)
            if not edge:
                return ""
            u, v = edge
            
            if u != v:
                graph[u].append(v)
                indegree[v] += 1
                

        order = []
        queue = deque()
        for i in range(26):
            if indegree[i] == 0:
                queue.append(i)
                

        while queue:
            char = queue.popleft()
            order.append(self.ord_chr(char))
            for adjchar in graph[char]:
                indegree[adjchar] -= 1
                if indegree[adjchar] == 0:
                    queue.append(adjchar)

        print(order, len(order))
        if len(order) != 26:
            return ""
        result = []
        for char in order:
            if char in participants:
                result.append(char)
        return "".join(result)




        