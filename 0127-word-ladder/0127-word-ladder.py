class Solution:
    def back_track(self, source, visited, endword, wordlist):
        if source == endword:
            return 0
        
        visited.add(source)
        ans = inf
        for word in wordlist:
            if word not in visited and self.is_valid(word, source):
                ans = min(ans, 1 + self.back_track(word, visited, endword, wordlist))
        visited.remove(source)
        return ans
    
    def is_valid(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count == 1
    
    def bfs(self, graph, source, endword):
        queue = deque([(source, 1)])
        visitied = set([source])

        while queue:
            word, depth = queue.popleft()
            if word == endword:
                return depth
            
            for wordneigh in graph[word]:
                if wordneigh not in visitied:
                    visitied.add(wordneigh)
                    queue.append((wordneigh, depth + 1))
        return 0

    def find_negih(self, word):
        words = []
        for i in range(len(word)):
            for j in range(26):
                neigh_word = word[:i] + chr(j + ord('a')) + word[i + 1:]
                words.append(neigh_word)
        return words

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # ans = self.back_track(beginWord, set(), endWord, wordList)
        # if ans == inf:
        #     return 0
        # return ans + 1
        wordList = set(wordList)
        wordList.add(beginWord)
        graph = {word: [] for word in wordList}
        for word in wordList:
            neigh_words = self.find_negih(word)
           
            for neigh_word in neigh_words:
                if neigh_word in wordList:
                    graph[word].append(neigh_word)
            
       
        return self.bfs(graph, beginWord, endWord)
        