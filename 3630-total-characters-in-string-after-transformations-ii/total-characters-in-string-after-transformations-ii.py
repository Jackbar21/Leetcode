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

### Solution after checking out 5'th editorial solution for this problem: 
### https://leetcode.com/problems/knight-dialer/
class Solution:
    # Helper method to multiply two matrices, taken from Knight Dialer Editorial!
    # (I.e. did not write this on my own...)
    # TODO: Write my own matrix multiplier function, just to show understanding!
    # But for now, using it so that I don't fail tests because of matrix multiplication bugs :P
    def multiply(self, A, B):
        result = [[0] * len(B[0]) for _ in range(len(A))]
        # print(f"{result=}, {A=}, {B=}")
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % self.MOD
        return result

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        self.MOD = MOD
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        ORD_A = ord("a")

        # Step 1: Build Actions Matrix
        matrix = [[0] * 26 for _ in range(26)]
        for i, letter in enumerate(ALPHABET):
            letter_index = ALPHABET.index(letter)
            count = nums[letter_index]
            for index in range(letter_index + 1, letter_index + 1 + count):
                assert matrix[i][index % 26] == 0
                matrix[i][index % 26] = 1
        self.matrix = matrix

        
        # for i, row in enumerate(matrix):
        #     # print(f"{ALPHABET[i]}: {row}")
        freq_dict = defaultdict(int)
        for letter in s:
            freq_dict[letter] += 1
        vector = [[freq_dict[letter] for letter in ALPHABET]]

        return sum(self.multiply(
            vector,
            self.matrixExp(t)
        )[0]) % MOD

    @cache
    def matrixExp(self, n):
        # self.matrix should already be defined. This will return value
        # of self.matrix to the power of 'n'
        matrix = self.matrix.copy()

        assert n >= 1
        if n == 1:
            return matrix
        
        if n % 2 == 1:
            return self.multiply(
                matrix,
                self.matrixExp(n - 1)
            )
        
        half_exp_matrix = self.matrixExp(n // 2)
        return self.multiply(
            half_exp_matrix,
            half_exp_matrix.copy()
        )
            

