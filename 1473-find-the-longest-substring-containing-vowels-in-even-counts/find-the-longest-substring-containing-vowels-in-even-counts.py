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
            # for j in range(i, len(self.s)):
            for j in range(longest_count + i, len(self.s)):
                if self.prefix_counts[j] ^ self.prefix_counts[i - 1] == 0:
                    longest_count = j - i + 1

        return longest_count

        # j > longest_count + i - 1
    


    # def evenVowelCounts(self, vowel_counts):
    #     return all([value % 2 == 0 for value in vowel_counts.values()])

    def isValidSubstring(self, i, j):
        # Want even number of vowels between i and j in s.
        # One way to check this is count number of vowels between index 0 to j,
        # and subtract number of values between 0 and i.
        return 0 == self.prefix_counts[j] ^ self.prefix_counts[i - 1]

        # vowel_counts = {vowel: 0 for vowel in 'aeiou'}
        # for vowel, count in self.prefix_counts[j].items():
        #     vowel_counts[vowel] += count
        
        # if i != 0:
        #     for vowel, count in self.prefix_counts[i - 1].items():
        #         vowel_counts[vowel] -= count
        
        # return self.evenVowelCounts(vowel_counts)