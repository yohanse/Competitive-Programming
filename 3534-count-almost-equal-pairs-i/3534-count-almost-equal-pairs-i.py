class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n=len(nums)
        def isAlmostEqual(a,b):
            if a==b:return True
            chances=2
            x=y=-1
            while a>0 or b>0:
                if a%10!=b%10:
                    chances-=1
                    if x==-1:
                        x=a%10
                        y=b%10
                    elif a%10!=y or b%10!=x:return False
                a//=10
                b//=10
            return chances==0
        return sum(isAlmostEqual(nums[i],nums[j]) for j in range(1,n) for i in range(j))