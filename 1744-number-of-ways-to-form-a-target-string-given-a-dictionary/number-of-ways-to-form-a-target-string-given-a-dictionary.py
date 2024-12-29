class Solution:
    def buildWordDict(self, word):
        d = defaultdict(dict)
        # inner_dict = defaultdict(list)
        inner_dict = defaultdict(int)
        for i in range(len(word) - 1, -1, -1):
            letter = word[i]
            # inner_dict[letter].append(i)
            inner_dict[letter] += 1
            # d[i] = defaultdict(list)
            # for key in inner_dict:
            #     d[i][key] = inner_dict[key].copy()
            d[i] = inner_dict.copy()
        return d
        # d = defaultdict(list)
        # for i, letter in enumerate(word):
        #     d[letter].append(i)
        # return d

    def numWays(self, words: List[str], target: str) -> int:
        self.MOD = pow(10, 9) + 7

        # word, start_index, freq_dict, banned_indices

        # For every word, make it a key in a dictionary 'word_to_dict', where the values
        # are dictionaries containing all valid indices in that word as the keys, and as
        # those indicides values a new dictionary of letter-to-index positions
        # word_to_dict = {word: self.buildWordDict(word) for word in words}

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
        self.index_to_freq_dict = index_to_freq_dict
        # print(f"{self.d=}")
        # return 0

        # print(f"{word_to_dict=}")
        # # return 0
        # for key in word_to_dict:
        #     print(f"{key=}, {word_to_dict[key]=}")

        # If word == j'th string in words, then 
        
        self.memo = {}
        return self.dp(0, 0) % self.MOD
        # return self.dpOld(0, initial_word_indices)
    
    def dp(self, word_index, target_index):
        if (word_index, target_index) in self.memo:
            return self.memo[(word_index, target_index)]
        
        if target_index >= len(self.target):
            return 1
        
        if word_index >= self.WORD_LENGTH:
            return 0 # since target_index still not at the end!
        
        letter = self.target[target_index]
        res = 0

        # Case 1: Don't consider word_index
        case1 = self.dp(word_index + 1, target_index)

        # Case 2: Do consider word_index. Can only do so if at least one available option
        num_options = self.index_to_freq_dict[word_index][letter]
        case2 = num_options * self.dp(word_index + 1, target_index + 1) if num_options > 0 else 0

        res = case1 + case2
        self.memo[(word_index, target_index)] = res
        return res

        # max_index = float("-inf")
        # for word in self.words:
        #     index_to_freq_dict = self.word_to_dict[word]
        #     d = index_to_freq_dict[word_index]
        #     # for index in d[letter]:
        #     #     res += self.dp(index + 1, target_index + 1)
        #     #     res %= self.MOD
        #     if len(d[letter]) > 0:
        #         max_index = max(max_index, d[letter][0])

        # for word in self.words:
        #     index_to_freq_dict = self.word_to_dict[word]
        #     d = index_to_freq_dict[word_index]
        #     for index in d[letter]:
        #         res += self.dp(index + 1, target_index + 1)
        #         res %= self.MOD

        for word in self.words:
            # res += self.dp(word_index + 1, target_index + int(word[word_index] == letter))
            # continue
            index_to_freq_dict = self.word_to_dict[word]
            freq_dict = index_to_freq_dict[word_index]
            if freq_dict[letter] > 0:
                # res += self.dp(word_index + 1, target_index + int(word[word_index] == letter))
                # Find first valid index
                idx = word_index
                while word[idx] != letter:
                    idx += 1
                res += self.dp(idx + 1, target_index + 1)
                # res += self.dp(word_index + 1, target_index + (word[word_index] == letter))

        self.memo[(word_index, target_index)] = res
        return res
    
    def dpOld(self, target_index, word_indices):
        if target_index >= len(self.target):
            return 1
        
        dp_key = tuple(word_indices) # EXPENSIVE
        if (target_index, dp_key) in self.memo:
            return self.memo[(target_index, word_indices)]
        
        letter = self.target[target_index]
        new_target_index = target_index + 1

        total_count = 0

        # Go through every single word, and for each one,
        # get all possible indices for grabbing letter, and
        # count valid number of ways from that decision
        for i, word in enumerate(self.words):
            d = self.word_to_dict[word]
            word_index = word_indices[i]
            # Want to do leftmost binary search to find first index in d[letter] that
            # is >= word_index.
            l, r = 0, len(d[letter])
            res = None
            while l <= r:
                mid = (l + r) // 2
                is_valid = d[letter][mid] >= word_index
                if is_valid:
                    # Good, look for some that are potentially even smaller!
                    r = mid - 1
                    res = mid
                else:
                    l = mid + 1
            
            if res is None:
                continue # No valid solutions!
            
            # Every index from mid onwards is valid!
            for idx in range(res, len(d[letter])):
                valid_index = d[letter][idx]
                # Consider the case where we add this element!
                word_indices[i] = valid_index + 1
                total_count += self.dp(target_index + 1, word_indices)
                word_indices[i] = word_index
        
        self.memo[(target_index, word_indices)] = total_count
        return total_count

