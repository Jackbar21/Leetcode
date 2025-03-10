class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels, consonants = {letter: collections.deque() for letter in "aeiou"}, collections.deque()
        l, res = 0, 0
        for r, letter in enumerate(word):
            if letter in "aeiou":
                vowels[letter].append(r)
            else:
                consonants.append(r)
            
            # Any solution with greater than k consonants is guaranteed to be invalid, 
            # so trim characters from the left-hand side!
            while len(consonants) > k:
                letter = word[l]
                if letter in "aeiou":
                    # assert vowels[letter].popleft() == l
                    vowels[letter].popleft()
                else:
                    # assert consonants.popleft() == l
                    consonants.popleft()
                # Loop Invariant
                l += 1

            # Valid case! Make sure to count all possible cases, i.e. by counting for any "redundant vowels"
            # at the beginning of the current valid substring!
            if len(consonants) == k and all(len(vowel_indices) >= 1 for vowel_indices in vowels.values()):
                bottleneck_index = consonants[0] if k > 0 else float("inf")
                for vowel_indices in vowels.values():
                    max_vowel_index = vowel_indices[-1]
                    if bottleneck_index > max_vowel_index:
                        bottleneck_index = max_vowel_index
                
                # Can delete everything up to BUT NOT INCLUDING bottleneck_index
                redundant_vowels = bottleneck_index - l # (bottleneck_index - 1) - l + 1
                res += redundant_vowels + 1

        return res
