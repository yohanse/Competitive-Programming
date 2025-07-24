class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # When I start with brute force solution we can try for all posibble choice I have not calculated the time and space complexity but I guess it would take as like inifinty :) 

        # let me go with the optimal one

        # detal I understand
        # when ever we are doing the operation we are increasing the array sum by sum(arr) - arr[i] i means the choosen index so if we have a number that is less than sum(arr) - arr[i] we can't create the array certainly because the sum is going up only so based on this the first I am going to try is to make the smallest number and I will containue

        # let simulate the example [9, 3, 5]

        # let sort it to make it easy [3, 5, 9]
        # arr = [1, 1, 1]

        # lets check for index=1     3 > 3 - 1
        # possible arr = [2, 1, 1]

        # check again 3 > 5 - 2
        3 == 3

        # if we start form the begining we will have multiple which means it very difficult to know

        # but one thing we be certain that the last number is going to be the maximum one which means we are to build the last lastely

        # like [9, 3, 5] so 9 will be build at last we can be certain that the target coomes from 
        # [1, 3, 5] because just assume [x, 3, 5] and ths sum hast to be 9 which leads as x + 3 + 5 = 9
        # so x = 1 that is why, by just going backward we can have only one path and we will go till the max number is less than or equal to 1

        if target == [1]:
            return True
        # lets go to the code
        sumi = sum(target)
        target = [-i for i in target]
        heapify(target)
        while target[0] < -1:
            max_num = -heappop(target)
            # max_num = x + the rest of array(sum - max_num)
            # max_num = x + sumi - max_num
            #2*max_num - sumi = x
            rest = sumi - max_num
            if rest == 0:
                return False

            x = (2*max_num - sumi)%rest
            if x == 0:
                x = rest
            # sumi = sumi - max_num + x
            sumi = sumi - max_num + x
            if x == max_num:
                return False
            heappush(target, -x)
        
        return  max(target) == -1