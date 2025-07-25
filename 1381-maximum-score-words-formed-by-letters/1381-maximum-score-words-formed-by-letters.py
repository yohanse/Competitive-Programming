class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Let me start with a bruteforce solution we generate all the subsequences of wrods list and check if we creat that subsequence with in our letter if so we can calulate the score and we will do this for every subsequence and find out the amximum score 

        # when we analyze the time complexity
        # genrating subsequence is 2**n n is len(words)
        # to check valid it won't takes us O(26) because 26 letter only and we can calculate the score while we are checking
        # function cost will be m, m is each word length

        # so final time complexity is 26*2**n*m which will pass

        # to optimize it we an add pruning by just stoping the resurion whenever if it is unvalid

        possible_letters = Counter(letters)
        def recursion(letters, index):
            if index == len(words):
                return 0
            
            # choose
            copy_letter = letters.copy()
            cost = choose_ans = 0
            for letter in words[index]:
                letters[letter] = letters.get(letter, 0) + 1
                cost += score[ord(letter) - ord('a')]
                if letters[letter] > possible_letters.get(letter, 0):
                    return recursion(copy_letter, index + 1)
            else:
                return max(recursion(letters, index + 1) + cost, recursion(copy_letter, index + 1))
        return recursion({}, 0)