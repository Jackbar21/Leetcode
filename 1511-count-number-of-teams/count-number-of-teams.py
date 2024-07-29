class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        for j in range(1,n-1):
            # How many elements exist in rating such that:
            # (1) element occurs BEFORE index j
            # (2) element's value is SMALLER than rating[j]
            num_before_inc, num_before_dec = 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    num_before_inc += 1
                elif rating[i] > rating[j]:
                    num_before_dec += 1
            
            # How many elements exist in rating such that:
            # (1) element occurs AFTER index j
            # (2) element's value is GREATER than rating[j]
            num_after_inc, num_after_dec = 0, 0
            for k in range(j+1,n):
                if rating[j] < rating[k]:
                    num_after_inc += 1
                elif rating[j] > rating[k]:
                    num_after_dec += 1
            
            # Example:
            # num_before = 2 [i1,i2] : rating[i1],rating[i2] < rating[j]
            # num_after = 3  [k1,k2,k3] : rating[j]< rating[k1],rating[k2],rating[k3]
            # 1. i1,j,k1 
            # 2. i1,j,k2
            # 3. i1,j,k3
            # 4. i2,j,k1
            # 5. i2,j,k2
            # 6. i2,j,k3
            # where 6 == 2 * 3
            res += num_before_inc * num_after_inc
            res += num_before_dec * num_after_dec
        
        return res
            