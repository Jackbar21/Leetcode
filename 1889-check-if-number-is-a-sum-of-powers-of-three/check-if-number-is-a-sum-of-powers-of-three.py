class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
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
