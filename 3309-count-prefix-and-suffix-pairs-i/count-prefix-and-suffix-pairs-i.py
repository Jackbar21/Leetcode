class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum((lambda str1, str2: str2.startswith(str1) and str2.endswith(str1))(words[i], words[j]) for i in range(len(words)) for j in range(i + 1, len(words)))