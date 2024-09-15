class Solution:
    def __init__(self):
        self.vowels = None
        self.s = None
        self.prefix_counts = None
    def findTheLongestSubstring(self, s: str) -> int:
        self.vowels = set("aeiou")
        self.s = s
        
        d = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        for shift, vowel in enumerate('aeiou'):
            d[vowel] = 1 << shift
        
        self.prefix_counts = {-1: 0}
        for i in range(len(self.s)):
            letter = self.s[i]
            self.prefix_counts[i] = d[letter] ^ self.prefix_counts[i - 1]

        # Now want to find max{j-i+1 | self.isValidSubstring(i, j)}
        longest_count = 0
        for i in range(len(self.s)):
            for j in range(longest_count + i, len(self.s)):
                # j starting from longest_count + i since only
                # want to update longest_count on valid substring
                # where j - i + 1 > longest_count <==> j >= longest_count + i
                if self.isValidSubstring(i, j):
                    longest_count = j - i + 1

        return longest_count

    def isValidSubstring(self, i, j):
        # Want even number of vowels between i and j in s.
        # One way to check this is count number of vowels between index 0 to j,
        # and subtract number of values between 0 and i.
        return 0 == self.prefix_counts[j] ^ self.prefix_counts[i - 1]