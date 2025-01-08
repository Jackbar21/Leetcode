class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(i < j and words[j].startswith(words[i]) and words[j].endswith(words[i]) for i in range(len(words)) for j in range(len(words)))