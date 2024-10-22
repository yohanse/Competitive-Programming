class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        leng1, leng2 = len(word1), len(word2)

        valid = [-1 for i in range(leng2)]

        l = leng2 - 1
        for i in range(leng1 - 1, -1, -1):
            if word1[i] == word2[l]:
                valid[l] = i
                l -= 1
                
            if l == -1:
                break
        print(valid)
        l = 0
        answer = []
        for i in range(leng1):
            if l == leng2:
                return answer
            if word1[i] == word2[l]:
                answer.append(i)
                l += 1

            elif l + 1 == leng2 or valid[l + 1] > i:
                print("aaa", answer)
                l += 1
                answer.append(i)
                for i in range(i + 1, leng1):
                    if l == leng2:
                        break

                    if word1[i] == word2[l]:
                        answer.append(i)
                        l += 1
                    
                return answer
            
            
        return []

            

        