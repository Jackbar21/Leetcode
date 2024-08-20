class Solution:
    def __init__(self):
        self.piles = None
        self.alice_memo = {}
        self.bob_memo = {}
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles, i, M = piles, 0, 1
        return self.alice(i, M)

    # MAX player
    # Returns Alice's maximum SCORE with optimal play from both Alice & Bob
    def alice(self, i, M):
        # i represents that piles[:i] have already been taken (i not inclusive)
        # M is taken from M, to generate X
        if (i, M) in self.alice_memo:
            return self.alice_memo[(i, M)]
        
        # No piles left to take, so return 0 score
        if i >= len(self.piles):
            assert i == len(self.piles)
            return 0

        # If can grab all remaining piles, then Alice should absolutely do so!
        if len(self.piles) - i <= 2 * M:
            return sum(self.piles[j] for j in range(i, len(self.piles)))
        
        num_stones = 0
        best_res = float("-inf")

        for X in range(1, 2 * M + 1):
            num_stones += self.piles[i + X - 1]
            num_piles_bob_takes = self.bob(i + X, max(M, X))
            new_M = max(M, X, num_piles_bob_takes)

            res = num_stones + self.alice(i + X + num_piles_bob_takes, new_M)
            best_res = max(best_res, res)

        self.alice_memo[(i, M)] = best_res
        return best_res

    # MIN player
    # Bob returns the NUMBER OF PILES he should grab to MINIMIZE Alice's score.
    def bob(self, i, M):
        # i represents that piles[:i] have already been taken (i not inclusive?)
        # M is taken from M, to generate X
        if (i, M) in self.bob_memo:
            return self.bob_memo[(i, M)]

        # No piles left to take, so return 0 moves
        if i >= len(self.piles):
            assert i == len(self.piles)
            return 0
        
        # If can grab all remaining piles, then Bob should absolutely do so!
        if len(self.piles) - i <= 2 * M:
            return len(self.piles) - i
        
        alice_score = float("inf") # Want to minimize!
        best_X = None
        for X in range(1, 2 * M + 1):
            # Don't care about how many stones Bob gets, only
            # care about minimizing Alice's total score (hehehe >:D)
            new_alice_score = self.alice(i + X, max(M, X))
            if new_alice_score < alice_score:
                alice_score = new_alice_score
                best_X = X
        
        self.bob_memo[(i, M)] = best_X
        return best_X
        

