class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = defaultdict(int)
        consonants = defaultdict(int)
        for char in s:
            if char in "aeiou":
                vowels[char] += 1
            else:
                consonants[char] += 1
        
        return max(vowels.values(), default = 0) + max(consonants.values(), default = 0)