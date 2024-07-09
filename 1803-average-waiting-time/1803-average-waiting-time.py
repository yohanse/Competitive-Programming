class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_time = wait_time = 0
        for arrival, time in customers:
            chef_time = max(chef_time, arrival) + time
            wait_time += (chef_time - arrival)
        
        return wait_time / len(customers)
