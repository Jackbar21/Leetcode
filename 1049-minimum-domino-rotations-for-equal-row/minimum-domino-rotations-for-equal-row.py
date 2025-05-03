class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Idea: Let's fix the first domino. Let's say tops[0] == X and bottoms[0] == Y.
        # Case 1: Make all of top row X (no switch on 0)
        # Case 2: Make all of top row Y (switch on 0)
        # Case 3: Make all of bottom row X (switch on 0)
        # Case 4: Make all of bottom row Y (no switch on 0)
        self.tops, self.bottoms = tops, bottoms
        assert len(tops) == len(bottoms)
        assert len(tops) > 0

        case1 = self.solver(solve_top = True, val = tops[0])
        case2 = self.solver(solve_top = True, val = bottoms[0])
        case3 = self.solver(solve_top = False, val = tops[0])
        case4 = self.solver(solve_top = False, val = bottoms[0])
        res = min(case1, case2, case3, case4)
        return res if res != float("inf") else -1
    
    # Returns float("inf") if no solution, not -1
    def solver(self, solve_top: bool, val: int) -> int:
        main, backup = (self.tops, self.bottoms) if solve_top else (self.bottoms, self.tops)
        
        res = 0
        for i, num in enumerate(main):
            # Val already on main!
            if val == num:
                continue
            
            # Val on backup, do rotation!
            if val == backup[i]:
                res += 1
                continue
            
            # No val, hence cannot be done
            return float("inf")
        
        return res