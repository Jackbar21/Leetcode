class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for j in range(1,n-1):
            num_before_inc, num_before_dec = 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    num_before_inc += 1
                elif rating[i] > rating[j]:
                    num_before_dec += 1
            
            num_after_inc, num_after_dec = 0, 0
            for k in range(j+1, n):
                if rating[j] < rating[k]:
                    num_after_inc += 1
                elif rating[j] > rating[k]:
                    num_after_dec += 1
            
            res += num_before_inc * num_after_inc
            res += num_before_dec * num_after_dec

        return res