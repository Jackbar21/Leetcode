class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for j in range(1,n-1):
            num_before_inc, num_before_dec = 0, 0
            # Want to find elements in rating such that:
            # (1) element occurs BEFORE j'th element in rating
            # (2) rating value of that element is SMALLER than rating[j]
            for i in range(j):
                if rating[i] < rating[j]:
                    num_before_inc += 1
                if rating[i] > rating[j]:
                    num_before_dec += 1
            
            num_after_inc, num_after_dec = 0, 0
            # Want to find elements in rating such. that:
            # (1) element occurs AFTER j'th element in rating
            # (2) rating value of that element is GREATER than rating[j]
            for k in range(j+1, n):
                if rating[j] < rating[k]:
                    num_after_inc += 1
                if rating[j] > rating[k]:
                    num_after_dec += 1
            
            res += num_before_inc * num_after_inc
            res += num_before_dec * num_after_dec

        return res