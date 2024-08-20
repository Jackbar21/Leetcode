class Solution:
    def __init__(self):
        self.piles = None
        self.alice_memo = {}
        self.bob_memo = {}
        # self.M = 1
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        # piles[i] = # of stones
        # M = 1 at beginning
        # can take stones in first X many piles, 1 <= X <= 2M
        # Afterwards, M = max(M, X)

        # At beginning, can only take up to two piles
        # If pick two piles, then M = max(M, X) = max(1, 2) = 2, meaning X now 1 <= X <= 4


        # Base Case: remaining number of piles <= X:
        #   Optimal Move: take all remaining piles
        i, M = 0, 1
        res = self.alice(i, M)
        # print(self.a)
        # print(self.b)
        return res

    # MAX player
    # Returns Alice's maximum SCORE with optimal play from both Alice & Bob
    def alice(self, i, M):
        if (i, M) in self.alice_memo:
            return self.alice_memo[(i, M)]
        # i represents that piles[:i] have already been taken (i not inclusive?)
        # M is taken from M, to generate X
        if i >= len(self.piles):
            # print(f"ALICE (BASE CASE 1): {len(self.piles) - i}")
            assert i == len(self.piles)
            return 0

        if len(self.piles) - i <= 2 * M:
            # print(f"ALICE (BASE CASE 2): {len(self.piles) - i}")
            return sum(self.piles[j] for j in range(i, len(self.piles)))
        
        num_stones = 0
        best_res = float("-inf")
        best_X = None
        best_num_stones = 0
        best_bob_X = None

        for X in range(1, 2 * M + 1):
            num_stones += self.piles[i + X - 1]
            num_piles_bob_takes = self.bob(i + X, max(M, X))
            new_M = max(M, num_piles_bob_takes)
            new_M = max(X, new_M)

            res = num_stones + self.alice(i + X + num_piles_bob_takes, new_M)
            # best_res = max(best_res, res)
            if res > best_res:
                best_res = res
                best_X = X
                best_num_stones = num_stones
                best_bob_X = num_piles_bob_takes

        # print(f"ALICE: {best_X}, {best_num_stones}")
        # self.a.append(best_X)
        # self.b.append(best_bob_X)
        self.alice_memo[(i, M)] = best_res
        return best_res

            # i, alice grabs X many
            # so i + 1, i + 2, ..., i + X - 1

            # res = self.alice(i + X, not is_alice_turn, max(M, X + 1))
            # if is_alice_turn:
            #     res += num_stones

            # if res >= best_res:
            #     best_res = res
            #     best_X = X
            # best_res = max(best_res, res)
        
        return best_res if best_res != float("-inf") else -1

    
    # MIN player
    # Bob returns the NUMBER OF PILES he should grab to MINIMIZE Alice's score.
    def bob(self, i, M):
        if (i, M) in self.bob_memo:
            return self.bob_memo[(i, M)]
        # i represents that piles[:i] have already been taken (i not inclusive?)
        # M is taken from M, to generate X
        if i >= len(self.piles):
            # print(f"BOB (BASE CASE 1): {len(self.piles) - i}")
            assert i == len(self.piles)
            return 0
        
        if len(self.piles) - i <= 2 * M:
            # return sum(self.piles[j] for j in range(i, len(self.piles)))
            # print(f"BOB (BASE CASE 2): {len(self.piles) - i}")
            return len(self.piles) - i
        
        alice_score = float("inf") # want to minimize!
        best_X = None
        for X in range(1, 2 * M + 1):
            # num_stones += self.piles[i + X - 1]
            new_alice_score = self.alice(i + X, max(M, X))
            if new_alice_score < alice_score:
                alice_score = new_alice_score
                best_X = X
        
        # print(f"BOB: {best_X}")
        self.bob_memo[(i, M)] = best_X
        return best_X
        
        # num_stones = 0
        # best_res = float("inf")
        # best_X = None
        # for X in range(2 * M):
        #     num_stones += self.piles[i + X]
        #     # res = num_stones + self.alice(i + X + 1)
        #     res = self.alice(i + X + 1, False)
        #     # best_res = min(best_res, res)
        #     if res < best_res:
        #         res = best_res
        #         best_X = X
        
        # M = max(M, X)
        # return best_res if best_res != float("inf") else -1
        

