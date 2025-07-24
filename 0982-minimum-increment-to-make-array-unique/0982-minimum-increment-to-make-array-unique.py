class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Could you give I minute to think about it 

        # Lets start with the bruteforce we can be greddy since we are adding one all the time we increasing each number by one so lets try to make different on the minuimum one and move up this will give us a time complexity of O(n**2) and O(1) space this n**2 happens when we have 99,999 ones and 100, 000 this will leda us ti n**2

        # but we can use one trhith if we have five similar number x after the operation they have to be x + 0, x + 1, x + 2, x + 3, x + 4 and we can calculate the time complexity prety easily so we will use sliding window techinque Is the number going to be consecutive with other not

    

        nums.sort()
        previous = -1
        operation = 0
        
        for i in range(len(nums)):
            # end of consecutive
            if nums[i] > previous:
                previous = nums[i]
            else:
                previous += 1
                operation += previous - nums[i]
        return operation

            