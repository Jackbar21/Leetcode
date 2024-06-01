class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Idea: use fixed array size of 26, since 26 letters
        # in alphabet, each corresponding to count of that letter,
        # to uniquely identify and group anagrams together
        d = {}
        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            
            t = tuple(alphabet)
            if t not in d:
                d[t] = []
            d[t].append(word)
        
        return d.values()
