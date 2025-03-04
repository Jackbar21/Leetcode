class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        self.cur_sum = 0
        def backtrack(power_of_three):
            if self.cur_sum == n:
                return True

            if max(power_of_three, self.cur_sum) > n:
                return False
            
            next_power = power_of_three * 3
            
            # Case 1: Add power_of_three
            self.cur_sum += power_of_three
            if backtrack(next_power):
                return True
            self.cur_sum -= power_of_three

            # Case 2: Ignore power_of_three
            return backtrack(next_power)
        
        # return backtrack(pow(3, 0))
        return backtrack(1)

        solutions = set([0])
        max_expo = math.floor(math.log(n, 3))
        power_of_three = pow(3, 0)
        for _ in range(max_expo + 1):
            solutions.update([solution + power_of_three for solution in solutions])

            # Loop Invariant
            power_of_three *= 3
            if n in solutions:
                return True
        
        return n in solutions
