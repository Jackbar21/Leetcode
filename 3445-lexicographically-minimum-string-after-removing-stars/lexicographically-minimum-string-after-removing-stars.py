class Solution:
    def clearStars(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {letter: [] for letter in ALPHABET} # -1 means NO index!

        # def getSmallestLetter():
        #     for letter in ALPHABET:
        #         if len

        deleted_indices = set()
        for i, char in enumerate(s):
            if char == "*":
                smallest_letter = min(letter for letter in ALPHABET if len(d[letter]) > 0)
                deleted_indices.add(d[smallest_letter].pop())
                continue
            
            d[char].append(i)
        
        return "".join(char for i, char in enumerate(s) if char != "*" and i not in deleted_indices)