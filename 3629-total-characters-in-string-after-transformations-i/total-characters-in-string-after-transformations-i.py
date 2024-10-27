class Solution:
    def __init__(self):
        self.memo = {}
        self.MAX_MOD = pow(10, 9) + 7

    def ASolver(self, t):
        if t < 26:
            return 1
        
        if t in self.memo:
            return self.memo[t]
        
        # After 26 iterations, a turns into "ab"
        # We can solve the "a" recursively. "b"
        # is just "a" after 1 transformation, 
        # so can also solve that recursively :)
        res = (self.ASolver(t - 26) + self.ASolver(t - 26 + 1)) % self.MAX_MOD
        self.memo[t] = res
        return res


    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = 0
        for letter in s:
            offset = ord(letter) - ord('a')
            count += self.ASolver(t + offset)
            count %= self.MAX_MOD
        
        return count

        