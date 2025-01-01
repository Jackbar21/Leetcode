class Solution:
    def maxScore(self, s: str) -> int:
        num_ones = s.count('1')
        num_zeroes = 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == "1":
                num_ones -= 1
            else:
                num_zeroes += 1
            
            res = max(res, num_ones + num_zeroes)
        
        return res