class Solution:
    def numTilings(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        self.n = n
        self.memo = {}
        res = self.dp(0, 0)
        #print(f"{self.memo=}")
        return res % MOD
    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        N = self.n

        if i >= N and j >= N:
            assert i == N and j == N # TODO: Return 1 IF AND ONLY IF i == N and j == N
            # return 1
            return i == N and j == N
        
        if i >= N:
            assert i == N
            # Can only put horizontal dominoes on bottom
            return (N - j) % 2 == 0

        if j >= N:
            assert j == N
            # Can only put horizontal dominoes on bottom
            return (N - i) % 2 == 0
        
        assert i < N and j < N
        
        # Case 1: Put a Domino vertically
        case1 = 0
        # Only possible if i and j are the same, as otherwise there's a collision!
        # if i == j and i < N and j < N:
        if i == j:
            case1 = self.dp(i + 1, j + 1)
            #print(f"{case1=}")
            assert case1 >= 0

        # Case 2: Put a Domino horizontally (either top or bottom!)
        case2 = 0
        # We can put a domino horizontally on either the top or the bottom.
        # When doing so, we must ensure we're not going out of bounds (i.e. i, j <= N)
        if i + 2 <= N:
            case2 += self.dp(i + 2, j)
        if j + 2 <= N:
            case2 += self.dp(i, j + 2)
        if i + 2 <= N and j + 2 <= N:
            case2 -= self.dp(i + 2, j + 2) # Do not double count!
        assert case2 >= 0

        # Case 3: Put a tromino with 'r' shape
        case3 = 0
        if i == j and i + 2 <= N:
            case3 = self.dp(i + 2, j + 1)

        # Case 4: Put a tromino with 'L' shape
        case4 = 0
        if i == j and j + 2 <= N:
            case4 = self.dp(i + 1, j + 2)
        
        # Case 5: Put a tromino with reverse-'r' shape
        case5 = 0
        if i == j - 1:
            case5 = self.dp(i + 2, j + 1)

        # Case 6: Put a tromino with reverse-'L' shape
        case6 = 0
        if i == j + 1:
            case6 = self.dp(i + 1, j + 2)

        res = case1 + case2 + case3 + case4 + case5 + case6
        self.memo[(i, j)] = res
        return res