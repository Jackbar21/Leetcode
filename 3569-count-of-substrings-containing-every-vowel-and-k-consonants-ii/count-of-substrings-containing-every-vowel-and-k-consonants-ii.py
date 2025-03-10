class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        # vowels = {letter: 0 for letter in "aeiou"}
        # consonants = 0
        vowels = {letter: collections.deque() for letter in "aeiou"}
        consonants = collections.deque()
        res = 0
        # add_by = 1
        # solutions = set()
        # queue = collections.deque()
        # redundant_prefix_length = None

        # O(N)
        # _prefix_vowels = []
        # d = {letter: 0 for letter in "aeiou"}
        # for letter in word:
        #     if letter in "aeiou":
        #         d[letter] += 1
        #     _prefix_vowels.append(d.copy())

        # print(f"{_prefix_vowels=}")
        # Get vowels & their frequencies of any subarray in O(1) time!
        # getSubarrayVowelCounts = lambda i, j: {letter: _prefix_vowels[j][letter] - (_prefix_vowels[i - 1][letter] if i > 0 else 0) for letter in "aeiou"}
        # getSubarrayConsonantsCount = lambda i, j: (j - i + 1) - sum(getSubarrayVowelCounts(i, j).values()) # lazyyyy
        # def getSubarrayVowelCounts(i, j):
        #     d = {}
        #     for letter in "aeiou":
        #         # print(f"alert: {j=}, {letter=}")
        #         for i, v in enumerate(prefix_vowels):
        #             # print(f"({i}): {v}")
        #         high = prefix_vowels[j][letter]
        #         low = (prefix_vowels[i - 1][letter] if i > 0 else 0)
        #         # print(f"{low=}")
        #         # print(f"{high=}")
        #         d[letter] = high - low
        #     return d

        # if word == "aoaiuefi":
        #     # print(f"{getSubarrayVowelCounts(3,4)=}")
        #     # print(f"{getSubarrayConsonantsCount(3,4)=}")
            


        l = 0
        for r, letter in enumerate(word):
            if letter in vowels:
                # vowels[letter] += 1
                vowels[letter].append(r)
            else:
                # consonants += 1
                consonants.append(r)
                # queue.append(r)
            
            while l < r and len(consonants) > k:
                # redundant_prefix_length = None
                letter = word[l]
                if letter in vowels:
                    # vowels[letter] -= 1
                    assert vowels[letter].popleft() == l
                    # res += vowels[letter] > 0
                else:
                    # consonants -= 1
                    assert consonants.popleft() == l
                    # assert queue.popleft() == l
                l += 1
            

            
            # while consonants == k and all(freq > 0 for freq in vowels.values()):
            #     # print(f"{l, r=}, c1, {vowels=}")
            #     res += 1
            #     letter = word[l]
            #     if letter in vowels:
            #         vowels[letter] -= 1
            #         res += vowels[letter] > 0
            #     else:
            #         consonants -= 1
            #     l += 1
            


            if len(consonants) == k and all(len(vowel_indices) > 0 for vowel_indices in vowels.values()):
                # i = l
                # while i < r and vowels.get(word[i], 0) > 1:
                #     solutions.add((i, r))
                #     i += 1
                # solutions.add((l, r))
                # # print(f"{l, r=}, c3")
                # res += 1
                # if k == 0:
                #     res += 1
                #     continue

                bottleneck_index = consonants[0] if k > 0 else float("inf")
                for vowel_indices in vowels.values():
                    bottleneck_index = min(bottleneck_index, vowel_indices[-1])
                
                # Can delete everything up to BUT NOT INCLUDING bottleneck_index
                redundant_vowels = (bottleneck_index - 1) - l + 1
                add_by = max(1, redundant_vowels + 1)

                # add_by = 1
                # i = l
                # # all_vowels = getSubarrayVowelCounts(l, r)
                # all_vowels = vowels.copy()
                # # while (letter := word[i]) in vowels and 
                # letter = word[i]
                # while letter in vowels and all_vowels[letter] > 1:
                #     all_vowels[letter] -= 1
                #     i += 1
                #     letter = word[i]
                # add_by += i - l
                res += add_by
                continue

                # Full string: word[l..r]
                # index of first consonant: queue[0]
                # assert len(queue) == k
                # if k == 0 or l == queue[0]:
                #     # string starts with consonant, so only 1 solution here (no redundant vowels prefix!)
                #     res += 1
                #     continue
                
                # index = queue[0]
                # assert l <= index - 1
                # # print(f"{l, index - 1=}")
                # prefix_vowels = getSubarrayVowelCounts(l, index - 1)
                # # print(f"{l, r=}")
                # all_vowels = getSubarrayVowelCounts(l, r)
                # add_by = 1
                # flag = False
                # for vowel, freq in prefix_vowels.items():
                #     if all_vowels[vowel] > freq:
                #         add_by += freq
                #     else:
                #         add_by += max(0, freq - 1)
                # res += max(1, add_by)

        
        # # print(f"{l=}")
        # res += 0 < l < r and consonants == k and all(freq > 0 for freq in vowels.values())
        # while l < r and consonants > k:
        #     letter = word[l]
        #     if letter in vowels:
        #         vowels[letter] -= 1
        #     else:
        #         consonants -= 1
        #     l += 1
        # while consonants == k and all(freq > 0 for freq in vowels.values()):
        #     res += 1
        #     letter = word[l]
        #     if letter in vowels:
        #         vowels[letter] -= 1
        #     else:
        #         consonants -= 1
        #     l += 1
        # while l < r and consonants > k:
        #     letter = word[l]
        #     if letter in vowels:
        #         vowels[letter] -= 1
        #         res += vowels[letter] > 0
        #     else:
        #         consonants -= 1
        #     l += 1
        
        # while l < r and consonants > k:
        #     letter = word[l]
        #     if letter in vowels:
        #         vowels[letter] -= 1
        #         # res += vowels[letter] > 0
        #     else:
        #         consonants -= 1
        #     l += 1
        # flag = False
        # while consonants == k and all(freq > 0 for freq in vowels.values()):
        #     flag = True
        #     # print(f"{l, r=}, c2, {vowels=}")
        #     res += 1
        #     # solutions.add((l,r))
        #     letter = word[l]
        #     if letter in vowels:
        #         vowels[letter] -= 1
        #         # res += vowels[letter] > 0
        #     else:
        #         consonants -= 1
        #     l += 1
        
        # return len(solutions)
        return res


# aaaaqkeiouaaalaaa
# l        r

# k = 2