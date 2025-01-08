class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(
            self.isPrefixAndSuffix(words[i], words[j])
            for i in range(len(words))
            for j in range(i + 1, len(words))
        )
    def isPrefixAndSuffix(self, str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)
        # return str2.startswith(str1) and str2[::-1].startswith(str1[::-1])