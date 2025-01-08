class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(words[j].startswith(words[i]) and words[j][::-1].startswith(words[i][::-1]) for i in range(len(words)) for j in range(i + 1, len(words)))