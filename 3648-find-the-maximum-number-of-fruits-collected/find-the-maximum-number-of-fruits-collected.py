class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # Observation 1: For child 1 to get from room (0, 0) to (n - 1, n - 1) in EXACTLY
        # n - 1 moves, means they must ALWAYS go (i, j) --> (i + 1, j + 1)

        # Now, we only have to focus on child 2 and child 3. Let c2 be the child starting at
        # (n - 1, 0), i.e. bottom-left; and c3 be the child starting at (0, n - 1), i.e. top-right.

        # Observation 2: c2 can only go rightwards, and c3 can only go downwards. Otherwise, c2 can
        # freely choose its up/down direction per move (-1,0,1), and similarly for c3's left/right
        # direction.

        # Observation 3: c2 and c3 can ONLY intersect with each other on the top-left-to-bottom-right
        # diagonal path, as otherwise one of them will have crossed the diagonal line -- making it
        # impossible to now reach the goal state due to the always move right / always move down
        # rules for c2 and c3, respectively.

        # Observation 4: Since child 1 has already consumed ALL the points inside the main diagonal, 
        # we can count those points in our solution initially, and assume there are 0 fruits there
        # left for c2 and c3 to pick up. That way we can run optimal cost paths for c2 and c3 to
        # the goal state with the "exactly n - 1 moves" restriction, as wanted by the problem.

        N = len(fruits)
        self.fruits = fruits

        res = 0
        for i in range(N):
            res += fruits[i][i]
            fruits[i][i] = 0
        
        # Observation 5: We could use UCS/Dijkstra's here, but since one of the two axis path direction
        # is fixed for c2 and c3 (right for c2 and down for c3), that only leaves the other direction
        # in question with n - 1 exact moves constraint. We can use DP instead for a total of
        # <= (n - 1) * (n - 1) subproblems, each in constant time, for total runtime O(N^2) complexity.
        self.memo_c2, self.memo_c3 = {}, {}
        res += self.dp_c2(0, N - 1)
        res += self.dp_c3(N - 1, 0)
        return res
    
    def dp_c2(self, i, j):
        if (i, j) in self.memo_c2:
            return self.memo_c2[(i, j)]

        fruits = self.fruits
        N = len(fruits)

        # Index i must always be +1, so terminal condition is when i == N - 1
        # assert i <= N - 1
        if i == N - 1:
            return fruits[i][j] if j == N - 1 else float("-inf")
        
        # Don't allow out of bounds solutions
        if j < 0 or j >= N:
            return float("-inf")
        
        fruit_amount = fruits[i][j]
        
        # Case 1: Move to (i + 1, j - 1)
        case1 = fruit_amount + self.dp_c2(i + 1, j - 1)

        # Case 2: Move to (i + 1, j)
        case2 = fruit_amount + self.dp_c2(i + 1, j)

        # Case 3: Move to (i + 1, j + 1)
        case3 = fruit_amount + self.dp_c2(i + 1, j + 1)

        res = case1 if case1 > case2 and case1 > case3 else case2 if case2 > case3 else case3
        self.memo_c2[(i, j)] = res
        return res

    def dp_c3(self, i, j):
        if (i, j) in self.memo_c3:
            return self.memo_c3[(i, j)]

        fruits = self.fruits
        N = len(fruits)

        # Index i must always be +1, so terminal condition is when i == N - 1
        # assert j <= N - 1
        if j == N - 1:
            return fruits[i][j] if i == N - 1 else float("-inf")
        
        # Don't allow out of bounds solutions
        if i < 0 or i >= N:
            return float("-inf")
        
        fruit_amount = fruits[i][j]
        
        # Case 1: Move to (i - 1, j + 1)
        case1 = fruit_amount + self.dp_c3(i - 1, j + 1)

        # Case 2: Move to (i, j + 1)
        case2 = fruit_amount + self.dp_c3(i, j + 1)

        # Case 3: Move to (i + 1, j + 1)
        case3 = fruit_amount + self.dp_c3(i + 1, j + 1)

        res = case1 if case1 > case2 and case1 > case3 else case2 if case2 > case3 else case3
        self.memo_c3[(i, j)] = res
        return res
