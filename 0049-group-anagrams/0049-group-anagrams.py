class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        table=[]
        for i in range(len(strs)):
            letter=[0]*26
            for j in strs[i]:
                letter[ord(j)-97]+=1
            if letter in table:
                p=table.index(letter)
                ans[p].append(strs[i])
            else:
                ans.append([strs[i]])
                table.append(letter)
        return ans