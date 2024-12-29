class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        self.MOD = pow(10, 9) + 7

        # Since all words have the same length, for every index i between 0 up to
        # that length - 1, as per Hint #1, we should have a frequency dict of each
        # letter at that index, for selecting it later on in target.
        self.WORD_LENGTH = len(words[0])
        self.target = target
        index_to_freq_dict = {}
        for word in words:
            for i, letter in enumerate(word):
                if i not in index_to_freq_dict:
                    index_to_freq_dict[i] = defaultdict(int)
                index_to_freq_dict[i][letter] += 1
        print(index_to_freq_dict)
        self.index_to_freq_dict = index_to_freq_dict
        self.memo = {}
        return self.dp(0, 0)
    
    def dp(self, word_index, target_index):
        if (word_index, target_index) in self.memo:
            return self.memo[(word_index, target_index)]
        
        if target_index >= len(self.target):
            return 1
        
        if word_index >= self.WORD_LENGTH:
            return 0 # since target_index still not at the end!
        
        letter = self.target[target_index]

        # Case 1: Don't consider word_index
        case1 = self.dp(word_index + 1, target_index) % self.MOD

        # Case 2: Do consider word_index. Can only do so if at least one available option
        num_options = self.index_to_freq_dict[word_index][letter]
        case2 = 0
        if num_options > 0:
            case2 = num_options * self.dp(word_index + 1, target_index + 1) % self.MOD

        res = (case1 + case2) % self.MOD
        self.memo[(word_index, target_index)] = res
        return res
