class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Let me start with brute we can gnenerate all possible divison of array and we can check if that didvsion satisfiy the requirement or not, if it satsifies we can count and continue the remaing
        # the time complexity will be 2**n for generating because we are dealing with two options either creating a new subarray or continue with the previous one and n will be the number of plan because we don't have to choose in seat we know how many we need to check it is o(1) because we can check while we are dividing so the time will be 2**number_of_plants

        # when we came to the optimal one we have to only focus only the plant except the edge case which means when we have odd number of seats the answer is 0 automatically because there is no valid didvision.

        # so how do we count let me show you with in example

        # example "PPSPSPPSSP"
        # first let firgure out what planrts matter the plants the matter is after completing the two seats except the last didvision and we will count that in our case the plants at 5, 6
        # so the first division has three choice first not include any plant, second choosing the first plant only and third choosing both plant like PPSPS, PPSPSP, PPSPSPP
        # so the answer is 3, right?

        # based on this we can count those kind of plants and multiple each by adding one
        # let me write it quickly


        seat_count = corridor.count("S")
        if seat_count == 0 or seat_count % 2:
            return 0

        seat_count_so_far = 0
        plant_count_so_far = 0
        ans = 1
        modulo = 10**9 + 7
        for letter in corridor:
            if letter == "S":
                seat_count_so_far += 1
                if seat_count_so_far%2 and seat_count_so_far != 1:
                    ans *= (plant_count_so_far + 1)
                    ans %= modulo
                plant_count_so_far = 0
            else:
                plant_count_so_far += 1
            
            
                
        return ans