class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # When I start  with the brute force we can choose subsequence of gas station tha we will use and check if they are valid and and place us to the destination so based on this we cna write the code with in time complexity of m*2**n where m is the length of the subsequence and n is the length of stationns 2**n is for choosing the subsequence and m is for validating since m might be lareg as n we can defintiely say it is n*2**n, and space complexity will be O(m) --> O(n). Additionally we can down the time complexity to 2**n by checking the validaity as we go. I think it is clear. the idea won't satisfy the time limit or constariants


        # Should I write the bruteforce appraoch shall I jump to the optimal one?

        # Could you give me a minute to think about the optimal one?

        # I hvae thinked about it 

        # What pattern I recognize is if we start form the initial we have two consider for the amount of fuel and the how many fuel are we using this thing would hurt because we have two manage two varaibles efficiently, I have think and it is not possible.

        # I will go with starting from the destination, if we use this apprach what we care is just only can I reach any valid destination and choose the minimum one fueling, I think it is clear right?

        # Let me start coding

        stations.append([target, 0])
        heap = []
        used_stations = 0
        print(stations)
        for i in range(len(stations)):
            if startFuel >= target:
                return used_stations
            
            while heap and startFuel < stations[i][0]:
                startFuel -= heappop(heap)
                used_stations += 1
            
            heappush(heap, -stations[i][1])
            if startFuel < stations[i][0]:
                return -1
        
        if startFuel >= target:
            return used_stations
        return -1