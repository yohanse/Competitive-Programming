class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        index=[]
        top=-1
        s+="("
        for i,char in enumerate(s):
            if char==")" and top!=-1 and stack[top]=="(":
                stack.pop()
                index.pop()
                top-=1
            else:
                stack.append(char)
                index.append(i)
                top+=1
        if len(index)==1:
            return len(s)-1
        ans=0
        index=[-1]+index
        for i in range(1,len(index)):
            ans=max(ans,index[i]-index[i-1]-1)
            
        return ans

