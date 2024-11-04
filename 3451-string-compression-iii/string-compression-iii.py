class Solution:
    def compressedString(self, word: str) -> str:
        res = []

        i = 0
        while i < len(word):
            letter = word[i]
            count = 1
            for offset in range(1, 9):
                index = i + offset
                if index < len(word) and letter == word[index]:
                    count += 1
                else:
                    break
            
            res.append(f"{count}{letter}")

            # Loop Invariant
            i += count

        return ''.join(res)