class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyza" # Extra 'a' at end for cyclic property :)
        d = {alphabet[i]: alphabet[i + 1] for i in range(len(alphabet) - 1)}
        index, cur_letter, STR2_LENGTH = 0, str2[0], len(str2)
        for letter in str1:
            if cur_letter == letter or cur_letter == d[letter]:
                index += 1
                if index >= STR2_LENGTH:
                    return True
                cur_letter = str2[index]
        return False
