class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        cur_time = 0

        for customer in customers:
            arrival, time = customer

            cur_time = max(cur_time, arrival) + time
            wait_time = cur_time - arrival
            res += wait_time

        return res / len(customers)