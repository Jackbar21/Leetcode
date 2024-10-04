class Solution:
    def getProduct(self, arr):
        base = 1
        for num in arr:
            base *= num
        return base
    def dividePlayers(self, skill: List[int]) -> int:
        # Idea: we want the minimum and maximum numbers/skills to be matched together.
        # Reason is that if you don't pair them together, and n > 2, then there will
        # at least exist two pairs of teams whose skills (as sums) do not match one another.
        # I.e. say min, max are the minimum and maximum skills, and for any two arbitrary 
        # skills, a,b such that min < a < b < max, only possible solutions are: 
        #       1. (min,a), (b,max)
        #       2. (min,b), (a,max)
        #       3. (a,b),   (min,max)
        # For 1. we have that:
        #     min + a
        #     < min + b, since a < b
        #     < max + b, since min < max
        #     ==> min + a != b + max, hence invalid solution
        # For 2. we have that:
        #     min + b
        #     < a + b, since min < a
        #     < a + max, since b < max
        #     ==> min + b != a + max, hence invalid solution
        # For 3. we have that: 
        #     This is the only solution that MIGHT be possible.
        #
        # For instance in Example 1 on the left, if I don't pair 1,5 together, then either:
        #   (a) I'll have a value smaller than 6 (but 5 will go with bigger element and be > 6)
        #   (b) a larger greater than 6 (but 1 will go with smaller than 5 and be < 6)
        skill.sort()
        TEAM_SUM = skill[0] + skill[-1]
        l, r = 0, len(skill) - 1
        res = 0
        while l < r:
            if skill[l] + skill[r] != TEAM_SUM:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res



        # Step 2: compute chemistry sum
        return self.getChemistrySum(pairs)
    
    def getChemistrySum(self, pairs):
        return sum(pair[0] * pair[1] for pair in pairs)