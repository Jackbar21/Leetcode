class Solution:
    def compressedString(self, word: str) -> str:
        res = []

        i = 0
        while i < len(word):
            letter = word[i]
            count = 1
            i += 1
            for offset in range(1, 9):
                # index = i + offset
                if i < len(word) and letter == word[i]:
                    count += 1
                    i += 1
                else:
                    break
            
            res.append(f"{count}{letter}")

            # Loop Invariant
            # i += count
            # i += 1

        return ''.join(res)
