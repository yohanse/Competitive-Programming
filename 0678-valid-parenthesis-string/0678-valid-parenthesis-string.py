class Solution:
    def checkValidString(self, s: str) -> bool:
        x=[]
        count=[]
        length=len(s)
        for i in range(length):
            if s[i]=='(':
                count.append(i)
            elif s[i]==')':
                if count==[]:
                    if x==[]:
                        return False
                    else:
                        x.pop()
                else:
                    count.pop()
            else:
                x.append(i)
        while x!=[] and count!=[]:
            if count.pop()>x.pop():
                return False
        if count==[]:
            return True
        return False
        