class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # return sum(
        #     words[j].startswith(words[i]) and words[j].endswith(words[i]) 
        #     for i in range(len(words)) 
        #     for j in range(i + 1, len(words))
        # )

        def isPrefixAndSuffix(str1, str2):
            is_prefix = str2.startswith(str1)
            is_suffix = str2.endswith(str1)
            return is_prefix and is_suffix

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count