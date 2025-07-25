class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Let me start with bruteforce what we can do over here is we can choose the minimum for the array and substract theat number to each elemnt and we will divde the arra by zeros what I mean is example [1, 2, 0, 3, 5, 0, 2, 0, 3] we will divide based on zeros like [1, 2], [3, 5], [2], [3] and we will continue the same thing until we got and empty array to anlayze the time complexity lest descripde somehthing for the recursion

        # state - arr
        # divide to max n
        # depth n

        # this algorith is divide and coqure so 
        # T(n) = T(a1) + T(a2) .... + T(am)
        # then n = a1 + a2 + a3 + .... + am - m + 1

        # we can use am aster theroem to know the time complexity but it is difficult but in wort case T(n) = T(1) + (n - 2)T(n - 2)
        # which will give us a time complexity of n**2
        # so it wont pass even it is great idea


        # lets go with the optimal
        # could you give me a minute to thinl about it 
        
        # from the above appraoch the problem arises when we have monutina shape subarrays
        # If a subarray is either increasing or decreasing the answer is max(sibarray)
        # so based on this I will assume all of the are decreasing and try to manage when Igo increasing

        # let me show you with in example
        # target = [3, 1, 5, 4, 2]
        # stack = []

        # index  = 0
        # for a single lement in the array the answer is it self
        # element, answer
        # stack = [(3, 3)]
        

        # indec = 1
        # it is decreasing so the answer the maximum one whihc is the first elemnt so no need to add operation
        # stack = [(3, 3), (1, 0)]

        # index = 2
        # This the mian part
        # 5 is grater than both 3 and 1
        # first we will check it it with one and 3
        # after all 5 will take the operations before plus the operation needed to make 5
        # whihch is 5 - the mini(number) that is popped out because we can over the that opeartion by including five with other subarray operations
        # the operation is = 3 + 5 - 1 = 7 
        # stack = [(5, 7)]

        # we will continue doing this but all the remaining numbers are less than 5 so no change

        # let me code it

        stack = [target[0]]
        operations = target[0]

        for i in range(len(target)):
            min_num = target[i]
            while stack and stack[-1] <= target[i]:
                min_num = min(min_num, stack.pop())
            

            operations += target[i] - min_num
            stack.append(target[i])
        return operations

        # let me run the code logically
        # target = [3, 1, 5, 4, 2]

