class Solution:
    def isValid(self, word):
        return word[0] in self.vowels and word[-1] in self.vowels

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        # self.vowels = vowels

        prefix_sums = [] # prefix_sums[i] == sum(self.isValid(word) for word in words[0..i])
        count = 0
        for word in words:
            # count += self.isValid(word)
            count += word[0] in vowels and word[-1] in vowels
            prefix_sums.append(count)
        
        # Since prefix_sums[i] == sum(self.isValid(word) for word in words[0..i]), notice that
        # for any i <= j, 
        #   prefix_sums[j] - prefix_sums[i - 1]
        #   == sum(self.isValid(word) for word in words[0..j]) 
        #      - sum(self.isValid(word) for word in words[0..i-1])
        #   == sum(self.isValid(word) for word in words[0..i-1]) 
        #      + sum(self.isValid(word) for word in words[i..j])
        #      - sum(self.isValid(word) for word in words[0..i-1])  
        #   == sum(self.isValid(word) for word in words[i..j]) 
        # ans = []
        # for l, r in queries:
        #     answer = prefix_sums[r] - (prefix_sums[l - 1] if l > 0 else 0)
        #     ans.append(answer)
        # return ans
        return [
            prefix_sums[r] - (prefix_sums[l - 1] if l > 0 else 0)
            for l, r in queries
        ]
