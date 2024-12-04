class Solution:
    def getNextLetter(self, letter):
        return self.d[letter]
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        d = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet) - 1):
            letter = alphabet[i]
            d[letter] = alphabet[i + 1]
        d['z'] = 'a'

        index, cur_letter, STR2_LENGTH = 0, str2[0], len(str2)
        for letter in str1:
            if cur_letter == letter or cur_letter == d[letter]:
                index += 1
                if index >= STR2_LENGTH:
                    return True
                cur_letter = str2[index]
        return False
