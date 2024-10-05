class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True

        if len(s2) < len(s1):
            return False

        dict_to_match = {}
        for letter in s1:
            dict_to_match[letter] = dict_to_match.get(letter, 0) + 1
        
        d = {}
        for i in range(len(s1)):
            letter = s2[i]
            d[letter] = d.get(letter, 0) + 1
        
        l, r = 0, len(s1)
        while d != dict_to_match and r < len(s2):
            letter_to_remove = s2[l]
            letter_to_add = s2[r]

            d[letter_to_remove] -= 1
            if d[letter_to_remove] == 0:
                del d[letter_to_remove]
            d[letter_to_add] = d.get(letter_to_add, 0) + 1

            l += 1
            r += 1
            # print(d)
        
        return d == dict_to_match
