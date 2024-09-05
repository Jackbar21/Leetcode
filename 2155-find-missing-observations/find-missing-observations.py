class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        mean --> f(i) / (m + n) for i in range(m + n) [for 0 <= i < m, f(i) == rolls[i] ]
             --> sum(rolls)/(m + n) + X/(m + n), where X is the sum of the remaining n rolls.
             --> (sum(rolls) + X) / (m + n)

        How do we get X?
        Well, simple algebra!
        mean == (sum(rolls) + X) / (m + n)
        <--> (m + n) * mean == sum(rolls) + X
        <--> (m + n) * mean - sum(rolls) == X
        <--> X == (m + n) * mean - sum(rolls)
        """
        m = len(rolls)
        X = (m + n) * mean - sum(rolls)

        # Base Case #1: n * 6 < X, which means that even if we made all n die
        # equal to their MAXIMUM value of 6, it is still not large enough
        # to reach the remaining X value that we need in order to make the
        # average of all dice rolls equal to 'mean'.
        if n * 6 < X:
            return []

        # Base Case #2: Similar to above, but in the case where n * 1 > X, where even
        # if we set all the remaining n die to their MINIMUM value of 1, it is
        # still larger than the remaining X value that we need in order to make
        # the average of all dice rolls equal to 'mean'.
        if n > X:
            return []
        
        assert n <= X and 6 * n >= X
        return self.convertSumToDice(X, n, [1, 2, 3, 4, 5, 6])
    
    def convertSumToDice(self, target_sum, n, possible_values):
        # Return a sequence of n dice rolls that sum up to target_sum
        assert n <= target_sum and 6 * n >= target_sum # If false, then problem is impossible

        # covers n == X and 6 * n == X cases 
        # for val in possible_values:
        #     if n * val == target_sum:
        #         return [val] * target_sum
        
        # mean = self.getMean(possible_values)
        # assert mean == 3.5

        base_num, remainder = target_sum // n, (target_sum % n)
        print(f"{base_num=}, {remainder=}, {n=}")
        res = [base_num] * n
        if remainder == 0:
            return res

        print(f"{n / remainder =}")
        # for i in range(0, n, n // remainder):
        for i in range(remainder):
            res[i] += 1
        
        return res

        target_sum / n

        3.5 * n > target_sum # make smaller, so add 1,2,3 to target_sum ?
        3.5 * n < target_sum # make larger, so add 4,5,6 to target_sum ?
        
    
    def getMean(self, arr):
        return sum(arr) / len(arr)
