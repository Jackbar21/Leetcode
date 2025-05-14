### Solution after checking out 5'th editorial solution for this problem: 
### https://leetcode.com/problems/knight-dialer/
class Solution:
    def multiply(self, A, B):
        # Let A be of dimensions ixj. Then B must be of dimensions jxk.
        # The resulting matrix will be of size ixk.
        #     [ a_11 a_12 . . . a_1j ]     [ b_11 b_12 . . . b_1k ]
        #     [ a_21 a_22 . . . a_2j ]     [ b_21 b_22 . . . b_2k ]
        # A = [ .                    ]  x  [ .                    ] = B
        #     [ .                    ]     [ .                    ]
        #     [ .                    ]     [ .                    ]
        #     [ a_i1 a_i2 . . . a_ij ]     [ b_j1 b_j2 . . . b_jk ]
        #
        # <==>
        #
        #     [ --------a_1--------- ]     [  |    | . . .     |  ]
        #     [ --------a_2--------- ]     [  |    | . . .     |  ]
        # A = [ .                    ]  x  [ b_1  b_2  . . .  b_j ] = B
        #     [ .                    ]     [  |    |           |  ]
        #     [ .                    ]     [  |    |           |  ]
        #     [ --------a_i--------- ]     [  |    | . . .     |  ]
        #
        # <==>
        #         [ (a_1 * b_1) (a_1 * b_2) . . . (a_1 * b_j) ]
        #         [ (a_2 * b_1) (a_2 * b_2) . . . (a_2 * b_j) ]
        # A x B = [ .                                         ], where '*' represents DOT-PRODUCT.
        #         [ .                                         ]
        #         [ .                                         ]
        #         [ (a_i * b_1) (a_i * b_2) . . . (a_i * b_j) ]
        B_cols = self.getColumns(B)
        res = [[0] * len(B_cols) for _ in range(len(A))]
        for i, a_vector in enumerate(A):
            for j, b_vector in enumerate(B_cols):
                res[i][j] = self.dotProduct(a_vector, b_vector) % self.MOD
        return res
    
    def getColumns(self, matrix):
        return [[matrix[ri][ci] for ri in range(len(matrix))] for ci in range(len(matrix[0]))]

    def dotProduct(self, v1, v2):
        # assert len(v1) == len(v2)
        return sum(map(lambda tup: tup[0] * tup[1], zip(v1, v2)))

    def matrixExp(self, n):
        if n in self.memo:
            return self.memo[n]

        # self.matrix should already be defined. This will return value
        # of self.matrix to the power of 'n'
        matrix = self.matrix

        # assert n >= 1
        if n == 1:
            return matrix
        
        if n % 2 == 1:
            res = self.multiply(
                matrix,
                self.matrixExp(n - 1)
            )
            self.memo[n] = res
            return res

        half_exp_matrix = self.matrixExp(n // 2)
        res = self.multiply(
            half_exp_matrix,
            half_exp_matrix
        )
        self.memo[n] = res
        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        self.MOD = MOD
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        ORD_A = ord("a")
        self.memo = {}

        # Step 1: Build Actions Matrix
        matrix = [[0] * 26 for _ in range(26)]
        for i, letter in enumerate(ALPHABET):
            letter_index = ALPHABET.index(letter)
            count = nums[letter_index]
            for index in range(letter_index + 1, letter_index + 1 + count):
                assert matrix[i][index % 26] == 0
                matrix[i][index % 26] = 1
        self.matrix = matrix

        freq_dict = defaultdict(int)
        for letter in s:
            freq_dict[letter] += 1
        vector = [[freq_dict[letter] for letter in ALPHABET]]

        return sum(self.multiply(
            vector,
            self.matrixExp(t)
        )[0]) % MOD

        # vector * (matrix)^t

### My initial solution (TLE) ###
"""
class Solution:
    def getConsecutiveLetters(self, letter, count):
        double_alphabet = self.DOUBLE_ALPHABET
        next_index = double_alphabet.index(letter) + 1
        return double_alphabet[next_index: next_index + count]

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        self.nums = nums
        self.memo = {}
        self.DOUBLE_ALPHABET = "abcdefghijklmnopqrstuvwxyz" * 2

        res = 0
        for letter in s:
            res = (res + self.dp(letter, t)) % MOD
        return res

    def dp(self, letter, t):
        MOD = pow(10, 9) + 7
        if (letter, t) in self.memo:
            return self.memo[(letter, t)]
        
        if t == 0:
            return 1
        
        res = 0
        count = self.nums[ord(letter) - 97] # ord("a") == 97
        # for consecutive_letter in self.getConsecutiveLetters(letter, count):
        double_alphabet = self.DOUBLE_ALPHABET
        next_index = double_alphabet.index(letter) + 1
        for index in range(next_index, next_index + count):
            consecutive_letter = double_alphabet[index]
            res = (res + self.dp(consecutive_letter, t - 1)) % MOD

        self.memo[(letter, t)] = res
        return res
"""
